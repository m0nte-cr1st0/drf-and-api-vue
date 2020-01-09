from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import ShipmentViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'shipments', ShipmentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]