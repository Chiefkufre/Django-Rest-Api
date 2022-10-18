# from turtle import title
from email import message
from pydoc import apropos
from rest_framework import authentication,generics, status, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Custom permission class
from api.mixins import IsStaffPermissionMixin
# end ----->

from api.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

# R-framework generic views pattern starts here

# ListcreateAPI routes -> this class list the endpoint data with a create option
class ProductCreateAPIView(
    IsStaffPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    # permission_classes = [permissions.IsAdminUser,IsStaffPermission]

    # authentication and permission are now inherited from the deault setting

    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     # authentication.TokenAuthentication,
    #     TokenAuthentication,
    #     ]

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAdminUser, IsStaffPermission]

    # permission_classes = [IsStaffPermission]


    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
    
    


class ProductListAPIView(
    IsStaffPermissionMixin,
    generics.ListAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(
    IsStaffPermissionMixin,
    generics.RetrieveAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # permission_classes = [permissions.IsAdminUser,IsStaffPermission]



class ProductUpdateAPIView(
    IsStaffPermissionMixin,
    generics.UpdateAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    # authentication and permission are now inherited from the deault setting
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication,
    #     ]
    # permission_classes = [permissions.IsAdminUser,IsStaffPermission]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            


class ProductDeleteAPIView(
    IsStaffPermissionMixin,
    generics.DestroyAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    # permission_classes = [permissions.IsAdminUser,IsStaffPermission]
    

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

# R-framework generic views pattern ends here
#

# <lass base  view with mixins starts here

class ProductMixinView(
    
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    generics.GenericAPIView
    
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

# Class base  view with mixins ends here


# function base  view with mixins starts here
@api_view(['GET', 'POST', 'PUT'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(product)
            return Response(data.data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True)
        return Response(data.data)

    if method == 'POST':
        product = get_object_or_404(Product, slug=kwargs['slug'])
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
    
    if method == "Delete":
        product = get_object_or_404(Product, pk=pk)
        data = ProductSerializer(product)

        if not product.DoesNotExist:
            product.delete()
            return Response(data.data, status=204)
        else:
            message.Message = "product does not exist"
    

    