from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'bio', 'profile_picture']

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key', 'user']

["serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user"]
