from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from .models import notify

class getnotificationSerializer(ModelSerializer):
    class Meta:
        model=notify
        fields='__all__'
