from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
#from .permisions import IsOwner,Istype
#from .utils import Util
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.decorators import login_required
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from rest_framework.response import Response
import json
from itertools import chain
import jwt
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from drf_multiple_model.views import FlatMultipleModelAPIView
from .serializer import aboutserializer,contactserializer,termserializer,faqserializer,privacyserializer,regionserializer,cityserializer
from.models import about,contact_us,help,privacy,terms,faq,region,city
from django.contrib.auth import authenticate,login,logout


# Create your views here.
@api_view(['GET'])
def getabout(request):
    lostp=about.objects.all()
    serializer=aboutserializer(lostp, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getcontact(request):
    lostp=contact_us.objects.all()
    serializer=contactserializer(lostp, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getprivacy(request):
    lostp=privacy.objects.all()
    serializer=privacyserializer(lostp, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getterm(request):
    lostp=terms.objects.all()
    serializer=termserializer(lostp, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getfaq(request):
    lostp=faq.objects.all()
    serializer=faqserializer(lostp, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getregion(request):
    lostp=region.objects.all()
    serializer=regionserializer(lostp, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getcity(request):
    lostp=city.objects.all()
    serializer=cityserializer(lostp, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def createcontact(request):
    data=request.data
    user=request.user
    if user.IsAuthenticated:
        data['asker']=user.id
    else:
        data['asker']=data['email']
    serializer=contactserializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response((serializer.data))
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)