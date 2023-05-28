from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import lost_P,found_P,lost_i,found_i,account,wanted_p
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class lostpSerializer(ModelSerializer):
    class Meta:
        model=lost_P
        fields='__all__'
    def create(self, validated_data):
        return lost_P.objects.create(**validated_data)
class wantedpSerializer(ModelSerializer):
    class Meta:
        model=wanted_p
        fields='__all__'
    def create(self, validated_data):
        return wanted_p.objects.create(**validated_data)
class foundpSerializer(ModelSerializer):
    class Meta:
        model=found_P
        fields='__all__'
    def create(self, validated_data):
        return found_P.objects.create(**validated_data)
class lostiSerializer(ModelSerializer):
    class Meta:
        model=lost_i
        fields='__all__'
    def create(self, validated_data):
        return lost_i.objects.create(**validated_data)
class foundiSerializer(ModelSerializer):
    class Meta:
        model=found_i
        fields='__all__'
    def create(self, validated_data):
        return found_i.objects.create(**validated_data)
class accountSerializer(ModelSerializer):
    password=serializers.CharField(max_length=128,write_only=True)
    class Meta:
        model=account
        fields='__all__'
    def create(self, validated_data):
        return account.objects.create(**validated_data)
class changeaccountserializer(ModelSerializer):
    class Meta:
        model=account
        fields=('first_name','last_name',
                'adress','p_number','city','region','email'
                )
class changepserializer(ModelSerializer):
    password=serializers.CharField(max_length=128,write_only=True)
    class Meta:
        model=account
        fields=('password',)
class registerserializer(ModelSerializer):
    password= serializers.CharField(max_length=128,min_length=8,write_only=True)
    class Meta:
        model =account
        fields=('password','username','first_name','last_name',
                'email','adress','p_number','user_type_id','city','region'
                )
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return account.objects.create(**validated_data)
class loginSerializer(ModelSerializer):
    password= serializers.CharField(write_only=True)
    email=serializers.EmailField()

    class Meta:
        model =account
        fields=('email','password','token')
        read_only_fields=['token']
    def validate(self, attrs):
        email=attrs.get('email','')
        password= attrs.get('password','')
        user= auth.authenticate(email=email,password=password)
        if not user:
            raise  AuthenticationFailed('invalid cridtional')
        if not user.is_active:
            raise  AuthenticationFailed('account disabled')

        return { 'email':user.email,'username':user.username,'token':user.token}
        return super().validate(attrs)