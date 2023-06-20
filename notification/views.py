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
from thread.models import account
from notification.models import notify
from .serializer import getnotificationSerializer

def sendnotification(rec,content):
    rec=account.objects.get(id=rec)
    notify.objects.create(rec=rec,content=content)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getnotfication(request):
    id=request.user.id
    data=notify.objects.filter(rec=id)
    serializer=getnotificationSerializer(data,many=True)
    return Response(serializer.data)
