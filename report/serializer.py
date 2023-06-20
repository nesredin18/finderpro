from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import repo,repo_type,reponumber,reportitemnumber
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class increasserializer(ModelSerializer):
    class Meta:
        model=reponumber
        fields='__all__'
    def create(self, validated_data):
        return reponumber.objects.create(**validated_data)
class itemincreasserializer(ModelSerializer):
    class Meta:
        model=reportitemnumber
        fields='__all__'
    def create(self, validated_data):
        return reportitemnumber.objects.create(**validated_data)
class reportserializer(ModelSerializer):
    class Meta:
        model=repo
        fields='__all__'
    def create(self, validated_data):
        return repo.objects.create(**validated_data)