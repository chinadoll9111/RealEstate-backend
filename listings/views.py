from rest_framework import generics, permissions
from .models import Listing, Inquiry
from .serializers import ListingSerializer, InquirySerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.views import TokenObtainPairView

# Register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Get all published listings
class ListingListView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        return Listing.objects.filter(published=True, sold=False)


# Single listing
class ListingDetailView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


# Search listing
class SearchListingView(generics.ListAPIView):
    serializer_class = ListingSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        return Listing.objects.filter(published=True, sold=False)


# Make inquiry
class InquiryCreateView(generics.CreateAPIView):
    serializer_class = InquirySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)