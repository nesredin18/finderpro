from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from.models import about,contact_us,help,privacy,terms,faq,region,city,contact
class aboutserializer(ModelSerializer):
    class Meta:
        model=about
        fields='__all__'
    def create(self, validated_data):
        return about.objects.create(**validated_data)
class contactserializer(ModelSerializer):
    class Meta:
        model=contact_us
        fields='__all__'
    def create(self, validated_data):
        return contact_us.objects.create(**validated_data)
class privacyserializer(ModelSerializer):
    class Meta:
        model=privacy
        fields='__all__'
    def create(self, validated_data):
        return privacy.objects.create(**validated_data)
class termserializer(ModelSerializer):
    class Meta:
        model=terms
        fields='__all__'
    def create(self, validated_data):
        return terms.objects.create(**validated_data)
class faqserializer(ModelSerializer):
    class Meta:
        model=faq
        fields='__all__'
    def create(self, validated_data):
        return faq.objects.create(**validated_data)
class regionserializer(ModelSerializer):
    class Meta:
        model=region
        fields='__all__'
    def create(self, validated_data):
        return region.objects.create(**validated_data)
class cityserializer(ModelSerializer):
    class Meta:
        model=city
        fields='__all__'
    def create(self, validated_data):
        return city.objects.create(**validated_data)
class contactserializer(ModelSerializer):
    class Meta:
        model=contact
        fields='__all__'
    def create(self, validated_data):
        return contact.objects.create(**validated_data)
