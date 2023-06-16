from rest_framework import routers
from .api import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register('api.categories', CategoryViewSet, basename='category')
router.register('api.products', ProductViewSet, basename='products')

urlpatterns = router.urls