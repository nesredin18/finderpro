from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from notification.views import sendnotification
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
from .serializer import reportserializer,increasserializer,itemincreasserializer
from .models import repo,repo_type,reponumber,reportitemnumber
from thread.models import account,lost_i,found_i,lost_P,found_P
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
        reported_item_id=data['reported_item']
        reported_item_type=data['reported_item_type']
        if reported_item_type=='lost-item' and lost_i.objects.filter(id=reported_item_id).exists():
            reported_item=lost_i.objects.get(id=reported_item_id)
        elif reported_item_type=='found-item' and found_i.objects.filter(id=reported_item_id).exists():
            reported_item=found_i.objects.get(id=reported_item_id)
        elif reported_item_type=='lost-person' and lost_P.objects.filter(id=reported_item_id).exists():
            reported_item=lost_P.objects.get(id=reported_item_id)
        elif reported_item_type=='found-person' and found_P.objects.filter(id=reported_item_id).exists():
            reported_item=found_P.objects.get(id=reported_item_id)
        else:
            return Response({'error':'invalid reported_item_type'},status=status.HTTP_400_BAD_REQUEST)
        if reportitemnumber.objects.filter(reported_item=reported_item,reported_item_type=reported_item_type).exists():
            repo_n=reportitemnumber.objects.get(reported_item=reported_item,reported_item_type=reported_item_type)
            repo_n.reported_item_n+=1
            repo_n.save()
            if repo_n.repo_n==3:
                sendnotification(reported,'your post have been reported 3 times')
            if repo_n.reported_item_n>=5:
                reported_item.delete()
        else:
            serializer2=itemincreasserializer(data=request.data)
            if serializer2.is_valid():
                serializer2.save()
            else:
                return Response(serializer2.errors,status=status.HTTP_400_BAD_REQUEST)
        
        if reponumber.objects.filter(reported=reported).exists():
            repo_n=reponumber.objects.get(reported=reported)
            repo_n.repo_n+=1
            repo_n.save()
            if repo_n.repo_n==3:
                sendnotification(reported,'you have been reported 3 times')
            if repo_n.repo_n>=5:
                reported=account.objects.get(id=reported)
                reported.is_active=False
                reported.save()
        else:
            serializer2=increasserializer(data=request.data)
            if serializer2.is_valid():
                serializer2.save()
            else:
                return Response(serializer2.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response((serializer.data))
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)