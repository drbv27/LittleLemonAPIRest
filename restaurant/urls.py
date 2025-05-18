from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet
from . import views

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('', include(router.urls)),
]
