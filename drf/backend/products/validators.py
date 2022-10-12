from rest_framework import serializers

from .models import Product

# Use validators to validate serializaters fields

def validate_title(value):
    qs = Product.objects.filter(title__iexact=True)
    if qs.exists():
        raise serializers.ValidationError(
            "Product with this title already exists"
        )
    return value

def validate_email(value):
    email = Product.objects.filter(email_iexact=True)
    if email.exists():
        serializers.ValidationError(msg="Email already exists")
    return value
    