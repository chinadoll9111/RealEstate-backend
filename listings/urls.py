from django.urls import path
from .views import (
    RegisterView,
    ListingListView,
    ListingDetailView,
    SearchListingView,
    InquiryCreateView
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('listings/', ListingListView.as_view()),
    path('listings/<int:pk>/', ListingDetailView.as_view()),
    path('search/', SearchListingView.as_view()),
    path('inquiry/', InquiryCreateView.as_view()),
]