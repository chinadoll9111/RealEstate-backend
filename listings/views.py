# listings/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Listing, Inquiry
from .serializers import ListingSerializer, InquirySerializer, RegisterSerializer, LoginSerializer

# --------------------------
# LISTINGS
# --------------------------
class ListingListAPIView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        queryset = Listing.objects.filter(published=True, sold=False)
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)
        return queryset


class ListingDetailAPIView(generics.RetrieveAPIView):
    queryset = Listing.objects.filter(published=True, sold=False)
    serializer_class = ListingSerializer
    lookup_field = 'pk'


class ListingSearchAPIView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        query = self.request.query_params.get('search', '')
        return Listing.objects.filter(
            Q(published=True, sold=False),
            Q(title__icontains=query) | Q(description__icontains=query)
        )

# --------------------------
# INQUIRIES
# --------------------------
class InquiryAPIView(generics.CreateAPIView):
    serializer_class = InquirySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# --------------------------
# USER REGISTRATION
# --------------------------
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            "user": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": f"Welcome {user.username}! Your account has been created."
        })


# --------------------------
# USER LOGIN
# --------------------------
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })