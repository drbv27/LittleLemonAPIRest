from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views  # Ensure this import is present
from rest_framework.authtoken.views import obtain_auth_token


# Create a router and register the viewset with it
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)  # Register the BookingViewSet with the router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('', include(router.urls)),  # Include the router URLs
    path('restaurant/booking/', include(router.urls)),  # Ensure this is included correctly
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),  # This endpoint allows users to log in and get a token

]
