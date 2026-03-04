# listings/urls.py

from django.urls import path
from .views import (
    ListingListAPIView,
    ListingDetailAPIView,
    ListingSearchAPIView,
    InquiryAPIView,
    RegisterAPIView,
    LoginAPIView
)

urlpatterns = [
    path('listings/', ListingListAPIView.as_view(), name='listing-list'),
    path('listings/<int:pk>/', ListingDetailAPIView.as_view(), name='listing-detail'),
    path('search/', ListingSearchAPIView.as_view(), name='listing-search'),
    path('inquiry/', InquiryAPIView.as_view(), name='listing-inquiry'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]