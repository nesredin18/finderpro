from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import message
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class sendserializer(ModelSerializer):
    class Meta:
        model=message
        fields='__all__'
    def create(self, validated_data):
        return message.objects.create(**validated_data)
class getmessageSerializer(ModelSerializer):
    class Meta:
        model=message
        fields='__all__'