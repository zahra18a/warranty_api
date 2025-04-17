from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, WarrantyViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'warranties', WarrantyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
