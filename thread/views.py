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
    serializer=lostpSerializer(lostp, many=True)
    return Response(serializer.data)
@api_view(["DELETE"])
def deletelostp(request,pk):
    lostp=lost_P.objects.get(id=pk)
    data= lostp
    serializer= lostpSerializer(data,many=False)
    lostp.delete()
    return Response(serializer.data)
@api_view(['PUT'])
def updatelostp(request, pk):
    #r=request
    #getlostpid(r,pk)
    data= request.data
    lostp=lost_P.objects.get(id=pk)
    serializer= lostpSerializer(lostp, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def createlostp(request):
    data= request.data
    lostp=lost_P.objects.create(
        user= account.objects.get(id=1),
        first_n= data['first_name'],
        last_n=data['last_name'],
        age= data['age'],
        height=data['height'],
        cloth=data['cloth'],
        mark=data['mark'],
        detail=data['detail'],
        adress=data['address'],
        region=data['region'],
        city=data['city'],
        p_type=person_type.objects.get(id=1),
    )
    serializer= lostpSerializer(lostp,many=False)
    return Response(serializer.data)



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
def deletefoundp(request,pk):
    foundp=found_P.objects.get(id=pk)
    data= foundp
    serializer= foundpSerializer(data,many=False)
    foundp.delete()
    return Response(serializer.data)
@api_view(['PUT'])
def updatefoundp(request, pk):
    #r=request
    #getlostpid(r,pk)
    data= request.data
    foundp=found_P.objects.get(id=pk)
    serializer= foundpSerializer(foundp, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def createfoundp(request):
    data= request.data
    lostp=found_P.objects.create(
        user= account.objects.get(id=1),
        first_n= data['first_name'],
        last_n=data['last_name'],
        age= data['age'],
        height=data['height'],
        cloth=data['cloth'],
        mark=data['mark'],
        detail=data['detail'],
        adress=data['address'],
        p_type=person_type.objects.get(id=1),
        region= data['region'],
        city= data['city'],
    )
    serializer= foundpSerializer(lostp,many=False)
    return Response(serializer.data)



@api_view(['GET'])
def getlosti(request):
    losti=lost_i.objects.all()
    serializer=lostiSerializer(losti, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getlostiid(request,pk):
    losti=lost_i.objects.get(id=pk)
    serializer1=lostiSerializer(losti, many=False)
    return Response(serializer1.data)
@api_view(["DELETE"])
def deletelosti(request,pk):
    losti=lost_i.objects.get(id=pk)
    data= losti
    serializer= lostiSerializer(data,many=False)
    losti.delete()
    return Response(serializer.data)
@api_view(['PUT'])
def updatelosti(request, pk):
    #r=request
    #getlostpid(r,pk)
    data= request.data
    losti=lost_i.objects.get(id=pk)
    serializer= lostiSerializer(losti, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def createlosti(request):
    data= request.data
    losti=lost_i.objects.create(
        user= account.objects.get(id=1),
        serial_n= data['serial_n'],
        region=data['region'],
        city= data['city'],
        detail=data['detail'],
        adress=data['address'],
        i_type=item_type.objects.get(id=1),
    )
    serializer= lostiSerializer(losti,many=False)
    return Response(serializer.data)



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
def deletefoundi(request,pk):
    foundi=found_i.objects.get(id=pk)
    data= foundi
    serializer= foundiSerializer(data,many=False)
    foundi.delete()
    return Response(serializer.data)
@api_view(['PUT'])
def updatefoundi(request, pk):
    #r=request
    #getlostpid(r,pk)
    data= request.data
    foundi=found_i.objects.get(id=pk)
    serializer= foundiSerializer(foundi, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def createfoundi(request):
    data= request.data
    foundi=found_i.objects.create(
        user=account.objects.get(id=1),
        serial_n= data['serial_n'],
        region=data['region'],
        city= data['city'],
        detail=data['detail'],
        adress=data['address'],
        i_type=item_type.objects.get(id=1),
    )
    serializer= foundiSerializer(foundi,many=False)
    return Response(serializer.data)

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
def deletewantedp(request,pk):
    lostp=wanted_p.objects.get(id=pk)
    data= lostp
    serializer= wantedpSerializer(data,many=False)
    lostp.delete()
    return Response(serializer.data)
@api_view(['PUT'])
def updatewantedp(request, pk):
    #r=request
    #getlostpid(r,pk)
    data= request.data
    lostp=wanted_p.objects.get(id=pk)
    serializer= wantedpSerializer(lostp, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def createwantedp(request):
    data= request.data
    lostp=wanted_p.objects.create(
        #user= request.user.email,
        user= account.objects.get(id=1),
        first_n= data['first_name'],
        last_n=data['last_name'],
        age= data['age'],
        height=data['height'],
        cloth=data['cloth'],
        mark=data['mark'],
        detail=data['detail'],
        adress=data['address'],
        region=data['region'],
        city=data['city'],
        reason=data['reason'],
        condition=data['condition'],
    )
    serializer= wantedpSerializer(lostp,many=False)
    return Response(serializer.data)


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
    losti=lost_i.objects.get(id=user)
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



@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsOwner])
def forgetpassword(request):
    #r=request
    #getlostpid(r,pk)
    pk=request.user.id
    data= request.data
    data['password']=make_password(data['password'])
    losti=account.objects.get(id=pk)
    serializer= changepserializer(losti, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("succusfully changed")
    return Response("there is error")

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
   