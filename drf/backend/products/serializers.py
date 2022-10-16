from wsgiref.validate import validator
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title
from api.serializers import UserSerializer

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )
    title = serializers.CharField(validators=[validate_title])
    user = UserSerializer(read_only=True)
    email = UserSerializer(read_only=True)
    class Meta:
        model = Product
        fields = [
            'edit_url',
            'email',
            'user',
            'url', 
            'pk',
            'title', 
            'content',
            'price', 
            'sale_price',
            'my_discount',
            'public' 
            ]
    
    # VALIDATOR ----> used to validate data before saving
    # def validate_title(self, value):
    #     qs = Product.object.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             'Title already exists for this product'
    #         )
    #     return value


    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     obj = super().create(**validated_data)
    #     return obj

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)


    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
    
    
       