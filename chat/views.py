from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.decorators import login_required
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from rest_framework.response import Response
import json
import jwt
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from drf_multiple_model.views import FlatMultipleModelAPIView
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.contrib.auth import authenticate,login,logout
from rest_framework.exceptions import AuthenticationFailed
from .serializer import sendserializer, getmessageSerializer
from .models import message
from django.db.models import Q
# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendmessage(request):
    if request.user.is_verfied==False:
        return Response({'error':'user is not verfied'},status=status.HTTP_400_BAD_REQUEST)
    data=request.data
    data['sender']=request.user.id
    if(data['sender']==data['rec']):
        return Response({'error':'cannot send message to self'},status=status.HTTP_400_BAD_REQUEST)
    serializer=sendserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response((serializer.data))
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getmessage(request):
    id=request.user.id
    data=message.objects.filter(Q(sender=id)|Q(rec=id))
    serializer=getmessageSerializer(data,many=True)
    return Response(serializer.data)
def getpersonmessage(request):
    data=request.data
    id=request.user.id
    rec=data['rec']
    data=message.objects.filter(sender=id,rec=rec)
    serializer=getmessageSerializer(data,many=True)
    return Response(serializer.data)
