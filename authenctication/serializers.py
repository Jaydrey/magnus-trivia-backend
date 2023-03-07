# importing rest framework serializers
from rest_framework import serializers
# django auth model import
from .models import User

class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()