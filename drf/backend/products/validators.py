from rest_framework import serializers

from .models import Product

# Use validators to validate serializaters fields

def validate_title(value):
    qs = Product.objects.filter(title__iexists=True)
    if qs.exists():
        raise serializers.ValidationError(
            "Product with this title already exists"
        )
    return value