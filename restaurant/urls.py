# restaurant/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views # Importa todas las vistas del módulo actual

# Router para las vistas de la API de la app 'restaurant'
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking') # `basename` es buena práctica

urlpatterns = [
    # URLs para MenuItemView y SingleMenuItemView
    path('menu/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),

]