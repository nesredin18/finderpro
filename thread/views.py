from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from .permisions import IsOwner,Istype
from .utils import Util
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
from .serializer import lostpSerializer,lostiSerializer,foundiSerializer,foundpSerializer,accountSerializer,registerserializer,loginSerializer,wantedpSerializer,changepserializer,changeaccountserializer
from .models import lost_P,found_P,lost_i,found_i,account,person_type,item_type,wanted_p
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.contrib.auth import authenticate,login,logout
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.gis.geoip2 import GeoIP2
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Q
from django.db.models import Sum, Case, When, Value, IntegerField
@api_view(['GET'])
def getRoutes(request):
    routes = [{
        'endpoint':'/thread/lost-item',
        'method':'GET',
        'body':None,
        'description':'returns All lost item'

    },
    {
        'endpoint':'/thread/found-item',
        'method':'GET',
        'body':None,
        'description':'returns All found item'
    }
    ,
    {
        'endpoint':'/thread/lost-person',
        'method':'GET',
        'body':None,
        'description':'returns All lost person'

    },
    {
        'endpoint':'/thread/found-person',
        'method':'GET',
        'body':None,
        'description':'returns All found person'    
    },
    {
        'endpoint':'/thread/wanted-person',
        'method':'GET',
        'body':None,
        'description':'returns All wanted person'
    },
    {
        'endpoint':'/thread/post-lost-item',
        'method':'POST',
        'body':None,
        'description':'creates a lost item'
    }
    ,
    {
        'endpoint':'/thread/post-found-item',
        'method':'POST',
        'body':None,
        'description':'creates a found item'
    },
    {
        'endpoint':'/thread/post-lost-person',
        'method':'POST',
        'body':None,
        'description':'creates a lost person'
    },
    {
        'endpoint':'/thread/post-found-person',
        'method':'POST',
        'body':None,
        'description':'creates a found person'
    },
    {
        'endpoint':'/thread/post-wanted-person',
        'method':'POST',
        'body':None,
        'description':'creates a wanted person'
    },
    {
        'endpoint':'/thread/delete-lost-item',
        'method':'DELETE',
        'body':None,
        'description':'deletes a lost item'
    },
    {   
        'endpoint':'/thread/delete-found-item',
        'method':'DELETE',
        'body':None,
        'description':'deletes a found item'
    },
    {
        'endpoint':'/thread/delete-lost-person',
        'method':'DELETE',
        'body':None,
        'description':'deletes a lost person'
    },
    {
        'endpoint':'/thread/delete-found-person',
        'method':'DELETE',
        'body':None,
        'description':'deletes a found person'
    },
    {
        'endpoint':'/thread/delete-wanted-person',
        'method':'DELETE',
        'body':None,
        'description':'deletes a wanted person'
    },
    {
        'endpoint':'/thread/update-lost-item',
        'method':'PUT',
        'body':None,
        'description':'updates a lost item'
    },
    {
        'endpoint':'/thread/update-found-item',
        'method':'PUT',
        'body':None,
        'description':'updates a found item'
    },
    {
        'endpoint':'/thread/update-lost-person',
        'method':'PUT',
        'body':None,
        'description':'updates a lost person'
    },
    {
        'endpoint':'/thread/update-found-person',
        'method':'PUT',
        'body':None,
        'description':'updates a found person'
    },
    {
        'endpoint':'/thread/update-wanted-person',
        'method':'PUT',
        'body':None,
        'description':'updates a wanted person'
    },
    {
        'endpoint':'/register',
        'method':'POST',
        'body':None,
        'description':'registers a user'
    },
    {
        'endpoint':'/login',
        'method':'POST',
        'body':None,
        'description':'logs in a user'
    },
    {
        'endpoint':'/logout',
        'method':'POST',
        'body':None,
        'description':'logs out a user'
    },
    ]

    return Response(routes)
@api_view(['GET'])
def getlostpid(request,pk):
    lostp=lost_P.objects.get(id=pk)
    serializer1=lostpSerializer(lostp, many=False)
    return Response(serializer1.data)
@api_view(['GET'])
def getlostp(request):
    lostp=lost_P.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer=lostpSerializer(lostp, many=True)
    return Response(serializer.data)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated,IsOwner])
def deletelostp(request,pk):
    obj=lost_P.objects.get(id=pk)
    if(request.user.id!=obj.user_id):
        return Response("you are not allowed")
    lostp=lost_P.objects.get(id=pk)
    data= lostp
    serializer= lostpSerializer(data,many=False)
    lostp.delete()
    return Response("succusfully deleted")
@api_view(['PUT'])

def updatelostp(request, pk):
    obj=lost_P.objects.get(id=pk)
    if(request.user.id!=obj.user_id):
        return Response("you are not allowed")
    #r=request
    #getlostpid(r,pk)
    data= request.data
    lostp=lost_P.objects.get(id=pk)
    serializer= lostpSerializer(lostp, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("there is error")
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createlostp(request):
    data=request.data
    data['user']=request.user.id
    parser_classes = (MultiPartParser, FormParser)
    serializer=lostpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response((serializer.data))
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getfoundp(request):
    foundP=found_P.objects.all()
    serializer1=foundpSerializer(foundP, many=True)
    return Response(serializer1.data)
@api_view(['GET'])
def getfoundpid(request,pk):
    foundP=found_P.objects.get(id=pk)
    serializer1=foundpSerializer(foundP, many=False)
    return Response(serializer1.data)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated,IsOwner])
def deletefoundp(request,pk):
    obj=found_P.objects.get(id=pk)
    if(request.user.id!=obj.user_id):
        return Response("you are not allowed")
    foundp=found_P.objects.get(id=pk)
    data= foundp
    serializer= foundpSerializer(data,many=False)
    foundp.delete()
    return Response(serializer.data)
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsOwner])
def updatefoundp(request, pk):
    obj=found_P.objects.get(id=pk)
    if(request.user.id!=obj.user_id):
        return Response("you are not allowed")
    #r=request
    #getlostpid(r,pk)
    data= request.data
    foundp=found_P.objects.get(id=pk)
    serializer= foundpSerializer(foundp, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createfoundp(request):
    data=request.data
    data['user']=request.user.id
    serializer=foundpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response((serializer.data))
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getlosti(request):
    losti=lost_i.objects.all()
    serializer=lostiSerializer(losti, many=True)
    return Response(serializer.data)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getlostiid(request,pk):
    losti=lost_i.objects.get(id=pk)
    serializer1=lostiSerializer(losti, many=False)
    return Response(serializer1.data)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated,IsOwner])
def deletelosti(request,pk):
    obj=lost_i.objects.get(id=pk)
    if(request.user.id!=obj.user_id):
        return Response("you are not allowed")
    losti=lost_i.objects.get(id=pk)
    data= losti
    serializer= lostiSerializer(data,many=False)
    losti.delete()
    return Response(serializer.data)
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsOwner])
def updatelosti(request, pk):
    obj=lost_i.objects.get(id=pk)
    if(request.user.id!=obj.user_id):
        return Response("you are not allowed")
    #r=request
    #getlostpid(r,pk)
    data= request.data
    losti=lost_i.objects.get(id=pk)
    serializer= lostiSerializer(losti, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createlosti(request):
    data=request.data
    data['user']=request.user.id
    serializer=lostiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response((serializer.data))
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getfoundi(request):
    foundi=found_i.objects.all()
    serializer1=foundiSerializer(foundi, many=True)
    return Response(serializer1.data)
@api_view(['GET'])
def getfoundiid(request,pk):
    foundi=found_i.objects.get(id=pk)
    serializer1=foundiSerializer(foundi, many=False)
    return Response(serializer1.data)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated,IsOwner])
def deletefoundi(request,pk):
    obj=found_i.objects.get(id=pk)
    if(request.user.id!=obj.user_id):
        return Response("you are not allowed")
    foundi=found_i.objects.get(id=pk)
    data= foundi
    serializer= foundiSerializer(data,many=False)
    foundi.delete()
    return Response(serializer.data)
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsOwner])
def updatefoundi(request, pk):
    obj=found_i.objects.get(id=pk)
    if(request.user.id!=obj.user_id):
        return Response("you are not allowed")
    #r=request
    #getlostpid(r,pk)
    data= request.data
    foundi=found_i.objects.get(id=pk)
    serializer= foundiSerializer(foundi, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createfoundi(request):
    data=request.data
    data['user']=request.user.id
    serializer=foundiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response((serializer.data))
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getwantedpid(request,pk):
    lostp=wanted_p.objects.get(id=pk)
    serializer1=wanted_p(lostp, many=False)
    return Response(serializer1.data)
@api_view(['GET'])
def getwantedp(request):
    lostp=wanted_p.objects.all()
    serializer=wantedpSerializer(lostp, many=True)
    return Response(serializer.data)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated,Istype])
def deletewantedp(request,pk):
    obj=wanted_p.objects.get(id=pk)
    if(request.user.id!=obj.user_id or request.user.user_type_id!=1):
        return Response("you are not allowed")
    lostp=wanted_p.objects.get(id=pk)
    data= lostp
    serializer= wantedpSerializer(data,many=False)
    lostp.delete()
    return Response(serializer.data)
@api_view(['PUT'])
@permission_classes([IsAuthenticated,Istype])
def updatewantedp(request, pk):
    obj=wanted_p.objects.get(id=pk)
    if(request.user.id!=obj.user_id or request.user.user_type_id!=1):
        return Response("you are not allowed")
    #r=request
    #getlostpid(r,pk)
    data= request.data
    lostp=wanted_p.objects.get(id=pk)
    serializer= wantedpSerializer(lostp, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated,Istype])
def createwantedp(request):
    if(request.user.user_type_id!=1):
        return Response("you are not allowed")
    data=request.data
    data['user']=request.user.id
    serializer=wantedpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response((serializer.data))
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sendveriagian(request):
    email=request.user.email
    user=account.objects.get(email=email)
    token = RefreshToken.for_user(user).access_token
    current_site=get_current_site(request).domain
    relativeLink=reverse('emailverify')
    absurl='http://'+current_site+relativeLink+"?token="+str(token)
    email_body='hi ' +user.username+' use link below to verify \n'+absurl 
    data={'email_body':email_body,'to_email':user.email,'e_subject':'verify'}
    Util.send_email(data)
        
    return Response(("email sent successfully"))
@api_view(['POST'])
def loginAccount(request):
    #data= request.data
    ser= loginSerializer(data=request.data)
    ser.is_valid(raise_exception=True)
    return Response(ser.data)
@api_view(['GET'])
def logoutAccount(request):
    logout(request)
    return Response("succefull logout")
@api_view(['POST'])
def registeruser(request):
    user=request.data
    serializer=registerserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user_data= serializer.data
        user=account.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site=get_current_site(request).domain
        relativeLink=reverse('emailverify')
        absurl='http://'+current_site+relativeLink+"?token="+str(token)
        email_body='hi ' +user.username+'use link below to verify \n'+absurl 
        data={'email_body':email_body,'to_email':user.email,'e_subject':'verify'}
        Util.send_email(data)
        
        return Response((serializer.data))
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def VerifyEmail(request):
    token=request.GET.get('token')
    try:
        payload =jwt.decode(token,settings.SECRET_KEY)
        user=account.objects.get(id=payload['user_id'])
        if user.is_verfied:
            return Response({'email':'already activated'})
        if not user.is_verfied:
            user.is_verfied=True
            user.save()
        return Response({'email':'Activated'})
    except jwt.ExpiredSignature as identifier:
        return Response({'error':'expired'})
    except jwt.exceptions.DecodeError as identifier:
        return Response({'error':'invalid token'})


@api_view(['GET'])
@permission_classes([IsAuthenticated,IsOwner])
def getaccount(request):
    user= request.user.id
    losti=account.objects.get(id=user)
    serializer=accountSerializer(losti, many=False)
    return Response(serializer.data)
@api_view(['GET'])
@permission_classes([IsAuthenticated,IsOwner])
def getaccountid(request,pk):
    losti=account.objects.get(id=pk)
    serializer1=accountSerializer(losti, many=False)
    return Response(serializer1.data)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated,IsOwner])
def deleteaccount(request):
    user=request.user.id
    losti=account.objects.get(id=user)
    serializer= accountSerializer(losti,many=False)
    losti.delete()
    return Response("succesfully deleted")
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsOwner])
def updateaccount(request):
    #r=request
    #getlostpid(r,pk)
    pk=request.user.id
    data= request.data
    losti=account.objects.get(id=pk)
    serializer= changeaccountserializer(losti, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("there is error")



@api_view(['POST'])
def forgetpassword(request):
    #r=request
    #getlostpid(r,pk)
    email=request.data['email']
    user=account.objects.get(email=email)
    if not user:
        return Response("user not found")
    token = RefreshToken.for_user(user).access_token
    current_site=get_current_site(request).domain
    relativeLink=reverse('resetpassword')
    absurl='http://'+current_site+relativeLink+"?token="+str(token)
    email_body='hi ' +user.username+'use link below to reset password \n'+absurl
    data={'email_body':email_body,'to_email':user.email,'e_subject':'reset password'}
    Util.send_email(data)
    return Response("email sent")
@api_view(['POST'])
def resetpassword(request):
    #r=request
    #getlostpid(r,pk)
    token=request.GET.get('token')
    password=request.data['password']
    try:
        payload =jwt.decode(token,settings.SECRET_KEY)
        user=account.objects.get(id=payload['user_id'])
        user.set_password(password)
        user.save()
        return Response("password reset")
    except jwt.ExpiredSignature as identifier:
        return Response({'error':'expired'})
    except jwt.exceptions.DecodeError as identifier:
        return Response({'error':'invalid token'})
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsOwner])
def changepassword(request):
    #r=request
    #getlostpid(r,pk)
    pk=request.user.id
    data= request.data
    oldp=data['old_password']
    oldpas=request.user.password

    print(oldp)
    print(oldpas)
    if not check_password(oldp,oldpas):
        return Response("pleas enter correct password")
    data['password']=make_password(data['password'])
    losti=account.objects.get(id=pk)
    serializer= changepserializer(losti, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("succusfully changed")
    return Response("there is error")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mypost(request):
    user = request.user

    lost_i_queryset = lost_i.objects.filter(user=user)
    lost_P_queryset = lost_P.objects.filter(user=user)
    found_i_queryset = found_i.objects.filter(user=user)
    found_P_queryset = found_P.objects.filter(user=user)

    sorted_queryset = sorted(
        chain(
            lost_i_queryset,
            lost_P_queryset,
            found_i_queryset,
            found_P_queryset
        ),
        key=lambda obj: obj.post_date,reverse=True
    )

    data = []

    for obj in sorted_queryset:
        if isinstance(obj, lost_i):
            serializer = lostiSerializer(obj)
        elif isinstance(obj, lost_P):
            serializer = lostpSerializer(obj)
        elif isinstance(obj, found_i):
            serializer = foundiSerializer(obj)
        elif isinstance(obj, found_P):
            serializer = foundpSerializer(obj)
        else:
            continue

        data.append(serializer.data)

    return Response(data)
@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsOwner])
def updatemypost(request, pk):
    data= request.data
    post_type = data['post_type']
    if post_type == "found person":
        obj=found_P.objects.get(id=pk)
        if(request.user.id!=obj.user_id):
            return Response("you are not allowed")
        return updatefoundp(request._request, pk)
    elif post_type == "lost person":
        obj=lost_P.objects.get(id=pk)
        if(request.user.id!=obj.user_id):
            return Response("you are not allowed")
        return updatelostp(request._request, pk)
    elif post_type == "found item":
        obj=found_i.objects.get(id=pk)
        if(request.user.id!=obj.user_id):
            return Response("you are not allowed")
        return updatefoundi(request._request, pk)
    elif post_type == "lost item":
        obj=lost_i.objects.get(id=pk)
        if(request.user.id!=obj.user_id):
            return Response("you are not allowed")
        return updatelosti(request._request, pk)
    else:
        return Response("Invalid post type")
    obj=found_P.objects.get(id=pk)
    if(request.user.id!=obj.user_id):
        return Response("you are not allowed")
    #r=request
    #getlostpid(r,pk)
    data= request.data
    foundp=found_P.objects.get(id=pk)
    serializer= foundpSerializer(foundp, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(["DELETE"])
@permission_classes([IsAuthenticated,IsOwner])
def deletemypost(request,pk):
    data= request.data
    post_type = data['post_type']
    if post_type == "found person":
        obj=found_P.objects.get(id=pk)
        if(request.user.id!=obj.user_id):
            return Response("you are not allowed")
        return deletefoundp(request._request, pk)
    elif post_type == "lost person":
        obj=lost_P.objects.get(id=pk)
        if(request.user.id!=obj.user_id):
            return Response("you are not allowed")
        return deletelostp(request._request, pk)
    elif post_type == "found item":
        obj=found_i.objects.get(id=pk)
        if(request.user.id!=obj.user_id):
            return Response("you are not allowed")
        return deletefoundi(request._request, pk)
    elif post_type == "lost item":
        obj=lost_i.objects.get(id=pk)
        if(request.user.id!=obj.user_id):
            return Response("you are not allowed")
        return deletelosti(request._request, pk)
    else:
        return Response("Invalid post type")




@api_view(['GET'])
def fetch_all_data(request):
    lost_i_queryset = lost_i.objects.all()
    lost_P_queryset = lost_P.objects.all()
    found_i_queryset = found_i.objects.all()
    found_P_queryset = found_P.objects.all()

    sorted_queryset = sorted(
        chain(
            lost_i_queryset,
            lost_P_queryset,
            found_i_queryset,
            found_P_queryset
        ),
        key=lambda obj: getattr(obj, 'post_date') if hasattr(obj, 'post_date') else getattr(obj, 'created_at'),
        reverse=True
    )

    data = []

    for obj in sorted_queryset:
        if isinstance(obj, lost_i):
            serializer = lostiSerializer(obj)
        elif isinstance(obj, lost_P):
            serializer = lostpSerializer(obj)
        elif isinstance(obj, found_i):
            serializer = foundiSerializer(obj)
        elif isinstance(obj, found_P):
            serializer = foundpSerializer(obj)
        else:
            continue

        data.append(serializer.data)

    return Response(data)

@api_view(['GET'])
def posts_near_you(request):
    user = request.user
    region = None
    city = None

    if user.is_authenticated:
        # Get location based on the user's city and region from registration
        # Replace 'city_field_name' and 'region_field_name' with the actual field names in your User model
        city = user.city
        region = user.region

    else:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # Get location based on user's current IP address
        g = GeoIP2()
        #ip = request.META.get('REMOTE_ADDR')
        location = g.city(ip)
        region = location['region']
        city = location['city']

    lost_i_queryset = lost_i.objects.filter(city=city, region=region)
    lost_P_queryset = lost_P.objects.filter(city=city, region=region)
    found_i_queryset = found_i.objects.filter(city=city, region=region)
    found_P_queryset = found_P.objects.filter(city=city, region=region)

    other_lost_i_queryset = lost_i.objects.exclude(city=city).exclude(region=region)
    other_lost_P_queryset = lost_P.objects.exclude(city=city).exclude(region=region)
    other_found_i_queryset = found_i.objects.exclude(city=city).exclude(region=region)
    other_found_P_queryset = found_P.objects.exclude(city=city).exclude(region=region)

    sorted_queryset = sorted(
        chain(
            lost_i_queryset,
            lost_P_queryset,
            found_i_queryset,
            found_P_queryset,
            other_lost_i_queryset,
            other_lost_P_queryset,
            other_found_i_queryset,
            other_found_P_queryset
        ),
        key=lambda obj: obj.post_date,reverse=True
    )
    data = []

    for obj in sorted_queryset:
        if isinstance(obj, lost_i):
            serializer = lostiSerializer(obj)
        elif isinstance(obj, lost_P):
            serializer = lostpSerializer(obj)
        elif isinstance(obj, found_i):
            serializer = foundiSerializer(obj)
        elif isinstance(obj, found_P):
            serializer = foundpSerializer(obj)
        else:
            continue

        data.append(serializer.data)
    return Response(data)

@api_view(['GET'])
def posts_in_your_region(request):
    user = request.user
    region = None
    city = None

    if user.is_authenticated:
        # Get location based on the user's city and region from registration
        # Replace 'city_field_name' and 'region_field_name' with the actual field names in your User model
        city = user.city
        region = user.region

    else:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # Get location based on user's current IP address
        g = GeoIP2()
        #ip = request.META.get('REMOTE_ADDR')
        location = g.city(ip)
        region = location['region']
        city = location['city']

    lost_i_queryset = lost_i.objects.filter(region=region)
    lost_P_queryset = lost_P.objects.filter(region=region)
    found_i_queryset = found_i.objects.filter(region=region)
    found_P_queryset = found_P.objects.filter(region=region)

    sorted_queryset = sorted(
        chain(
            lost_i_queryset,
            lost_P_queryset,
            found_i_queryset,
            found_P_queryset
        ),
        key=lambda obj: obj.post_date,reverse=True
    )

    data = []

    for obj in sorted_queryset:
        if isinstance(obj, lost_i):
            serializer = lostiSerializer(obj)
        elif isinstance(obj, lost_P):
            serializer = lostpSerializer(obj)
        elif isinstance(obj, found_i):
            serializer = foundiSerializer(obj)
        elif isinstance(obj, found_P):
            serializer = foundpSerializer(obj)
        else:
            continue

        data.append(serializer.data)

    return Response(data)

@api_view(['GET'])
def posts_in_your_city(request):
    user = request.user
    region = None
    city = None

    if user.is_authenticated:
        # Get location based on the user's city and region from registration
        # Replace 'city_field_name' and 'region_field_name' with the actual field names in your User model
        city = user.city
        region = user.region

    else:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # Get location based on user's current IP address
        g = GeoIP2()
        #ip = request.META.get('REMOTE_ADDR')
        location = g.city(ip)
        region = location['region']
        city = location['city']

    lost_i_queryset = lost_i.objects.filter(city=city)
    lost_P_queryset = lost_P.objects.filter(city=city)
    found_i_queryset = found_i.objects.filter(city=city)
    found_P_queryset = found_P.objects.filter(city=city)

    sorted_queryset = sorted(
        chain(
            lost_i_queryset,
            lost_P_queryset,
            found_i_queryset,
            found_P_queryset
        ),
        key=lambda obj: obj.post_date,reverse=True
    )

    data = []

    for obj in sorted_queryset:
        if isinstance(obj, lost_i):
            serializer = lostiSerializer(obj)
        elif isinstance(obj, lost_P):
            serializer = lostpSerializer(obj)
        elif isinstance(obj, found_i):
            serializer = foundiSerializer(obj)
        elif isinstance(obj, found_P):
            serializer = foundpSerializer(obj)
        else:
            continue

        data.append(serializer.data)

    return Response(data)






@api_view(['GET'])
def search_products(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'

    # Split the query into individual search terms
    search_terms = query.split()

    # Define the search conditions for each table
    found_p_conditions = []
    found_i_conditions = []
    lost_p_conditions = []
    lost_i_conditions = []

    # Populate the search conditions for each table based on the search terms
    for term in search_terms:
        found_p_conditions.extend([
            Q(first_name__icontains=term),
            Q(last_name__icontains=term),
            Q(age__icontains=term),
            Q(height__icontains=term),
            Q(gender__icontains=term),
            Q(region__icontains=term),
            Q(city__icontains=term),
            Q(cloth__icontains=term),
            Q(mark__icontains=term),
            Q(detail__icontains=term),
            Q(address__icontains=term),
        ])
        found_i_conditions.extend([
            Q(region__icontains=term),
            Q(city__icontains=term),
            Q(detail__icontains=term),
            Q(post_date__icontains=term),
            Q(serial_n__icontains=term),
            Q(adress__icontains=term),
        ])
        lost_p_conditions.extend([
            Q(first_name__icontains=term),
            Q(last_name__icontains=term),
            Q(age__icontains=term),
            Q(height__icontains=term),
            Q(gender__icontains=term),
            Q(region__icontains=term),
            Q(city__icontains=term),
            Q(cloth__icontains=term),
            Q(mark__icontains=term),
            Q(detail__icontains=term),
            Q(address__icontains=term),
        ])
        lost_i_conditions.extend([
            Q(region__icontains=term),
            Q(city__icontains=term),
            Q(detail__icontains=term),
            Q(post_date__icontains=term),
            Q(serial_n__icontains=term),
            Q(adress__icontains=term),
        ])

    # Combine the conditions using OR operator for each table
    found_p_query_filter = Q()
    found_i_query_filter = Q()
    lost_p_query_filter = Q()
    lost_i_query_filter = Q()
    
    for condition in found_p_conditions:
        found_p_query_filter |= condition
    for condition in found_i_conditions:
        found_i_query_filter |= condition
    for condition in lost_p_conditions:
        lost_p_query_filter |= condition
    for condition in lost_i_conditions:
        lost_i_query_filter |= condition

    # Perform the search on each table
    found_p_results = found_P.objects.filter(found_p_query_filter).annotate(
        num_matches=Sum(
            Case(When(found_p_query_filter, then=Value(1)), default=Value(0), output_field=IntegerField())
        )
    )
    found_i_results = found_i.objects.filter(found_i_query_filter).annotate(
        num_matches=Sum(
            Case(When(found_i_query_filter, then=Value(1)), default=Value(0), output_field=IntegerField())
        )
    )
    lost_p_results = lost_P.objects.filter(lost_p_query_filter).annotate(
        num_matches=Sum(
            Case(When(lost_p_query_filter, then=Value(1)), default=Value(0), output_field=IntegerField())
        )
    )
    lost_i_results = lost_i.objects.filter(lost_i_query_filter).annotate(
        num_matches=Sum(
            Case(When(lost_i_query_filter, then=Value(1)), default=Value(0), output_field=IntegerField())
        )
    )

    # Concatenate the results from all tables
    all_results = list(found_p_results) + list(found_i_results) + list(lost_p_results) + list(lost_i_results)

    # Sort the results by the number of matching terms in descending order
    sorted_results = sorted(all_results, key=lambda x: x.num_matches, reverse=True)

    # Serialize the sorted results using respective serializers
    data = []

    for obj in sorted_results:
        if isinstance(obj, lost_i):
            serializer = lostiSerializer(obj)
        elif isinstance(obj, lost_P):
            serializer = lostpSerializer(obj)
        elif isinstance(obj, found_i):
            serializer = foundiSerializer(obj)
        elif isinstance(obj, found_P):
            serializer = foundpSerializer(obj)
        else:
            continue

        data.append(serializer.data)

    return Response(data)



 

























  
def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
     email=request.user.email
     print(email)
     o=generateOTP()
     htmlgen = '<p>Your OTP is <strong>o</strong></p>'
     send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
     #return HttpResponse(o)
   
@api_view(['GET'])
def getThread(request):
    if request.user.is_authenticated:
        reg=request.user.region
        ci=request.user.city
        lostp=lost_P.objects.filter(region=reg)
        losti=lost_i.objects.filter(region=reg)
        foundp=found_P.objects.filter(region=reg)
        foundi=found_i.objects.filter(region=reg)
        lostpr=lost_P.objects.filter(city=ci)
        lostir=lost_i.objects.filter(city=ci)
        foundpr=found_P.objects.filter(city=ci)
        foundir=found_i.objects.filter(city=ci)
        lostpp=lost_P.objects.all().exclude(region=reg).exclude(city=ci)
        lostip=lost_i.objects.all().exclude(region=reg).exclude(city=ci)
        foundpp=found_P.objects.all().exclude(region=reg).exclude(city=ci)
        foundip=found_i.objects.all().exclude(region=reg).exclude(city=ci)
        seria1=lostpSerializer(lostp,many=True)
        seria2=lostiSerializer(losti,many=True)
        seria3=foundpSerializer(foundp,many=True)
        seria4=foundiSerializer(foundi,many=True)
        seria5=lostpSerializer(lostpr,many=True)
        seria6=lostiSerializer(lostir,many=True)
        seria7=foundpSerializer(foundpr,many=True)
        seria8=foundiSerializer(foundir,many=True)
        seria9=lostpSerializer(lostpp,many=True)
        seria10=lostiSerializer(lostip,many=True)
        seria11=foundpSerializer(foundpp,many=True)
        seria12=foundiSerializer(foundip,many=True)
        result1=seria5.data+seria6.data+seria7.data+seria8.data
        result2=seria1.data+seria2.data+seria3.data+seria4.data
        result3=seria9.data+seria10.data+seria11.data+seria12.data
        result=result1+result2+result3
        return Response(result)

    lostp=found_i.objects.all()
    losti=lost_i.objects.all()
    foundp=found_P.objects.all()
    foundi=found_i.objects.all()
    seria1=lostpSerializer(lostp,many=True)
    seria2=lostiSerializer(losti,many=True)
    seria3=foundpSerializer(foundp,many=True)
    seria4=foundiSerializer(foundi,many=True)
    result=seria1.data+seria2.data+seria3.data+seria4.data
    return Response(result)

@api_view(['GET'])
def getallth(request):
    lostp=lost_P.objects.all()
    losti=lost_i.objects.all()
    foundp=found_P.objects.all()
    foundi=found_i.objects.all()
    seria1=lostpSerializer(lostp,many=True)
    seria2=lostiSerializer(losti,many=True)
    seria3=foundpSerializer(foundp,many=True)
    seria4=foundiSerializer(foundi,many=True)
    result=seria1.data+seria2.data+seria3.data+seria4.data
    return Response(result)
