# littlelemon/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views as restaurant_views # Importa las vistas de tu app 'restaurant'
from rest_framework.authtoken.views import obtain_auth_token

# Router para BookingViewSet (API) - Definido globalmente como lo tenías
# Esto crea URLs como /tables/ y /restaurant/booking/tables/
router = DefaultRouter()
# Asegúrate de que 'views.BookingViewSet' se refiera a 'restaurant_views.BookingViewSet'
router.register(r'tables', restaurant_views.BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),

    # NUEVA RUTA PARA TU VISTA HTML PRINCIPAL
    path('home/', restaurant_views.vista_principal, name='home'),

    # URLs de la API para la app 'restaurant' (solo menu, el booking se maneja por el router global)
    path('restaurant/', include('restaurant.urls')), # Esto incluirá /restaurant/menu/ y /restaurant/menu/<pk>/

    # URLs generadas por el router global para BookingViewSet
    # Esto crea:
    # /tables/
    # /tables/<pk>/
    path('', include(router.urls)), # Para que /tables/ funcione directamente

    # Esto también incluye las URLs del MISMO router, pero bajo el prefijo /restaurant/booking/
    # Esto crea:
    # /restaurant/booking/tables/
    # /restaurant/booking/tables/<pk>/
    path('restaurant/booking/', include(router.urls)),

    # URLs para autenticación
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
]