from rest_framework import viewsets


from .models import Product
from .serializers import ProductSerializer

from api.mixins import StaffPermissionMixin


class ProductViewSet(
    StaffPermissionMixin,
    viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
