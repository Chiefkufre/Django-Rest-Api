from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(read_only=True)