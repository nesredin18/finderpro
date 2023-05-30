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
from .serializer import reportserializer,increasserializer
from .models import repo,repo_type,reponumber
# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def report(request):
    if request.user.is_verfied==False:
        return Response({'error':'user is not verfied'},status=status.HTTP_400_BAD_REQUEST)
    data=request.data
    
    data['reporter']=request.user.id
    if(data['reporter']==data['reported']):
        return Response({'error:cannot report yourself'},status=status.HTTP_400_BAD_REQUEST)
    serializer=reportserializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        reported=data['reported']
        if reponumber.objects.filter(reported=reported).exists():
            repo_n=reponumber.objects.get(reported=reported)
            repo_n.repo_n+=1
            repo_n.save()
        else:
            serializer2=increasserializer(data={'reported':reported})
            if serializer2.is_valid():
                serializer2.save()
            else:
                return Response(serializer2.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response((serializer.data))
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)