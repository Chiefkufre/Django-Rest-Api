from rest_framework.routers import DefaultRouter

from products.viewset import ProductViewSet

router = DefaultRouter()
router.register('products-abc', ProductViewSet, 
basename='products')


urlpatterns = router.urls