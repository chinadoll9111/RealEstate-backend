from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return JsonResponse({
        "message": "Real Estate API is running",
        "endpoints": {
            "listings": "/api/listings/",
            "search": "/api/search/?search=",
            "login": "/api/token/"
        }
    })

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    # JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API app routes
    path('api/', include('listings.urls')),
]