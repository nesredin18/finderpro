from django.db import models
from django.contrib.auth.models import AbstractUser
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
class user_type(models.Model):
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type
class account(AbstractUser):
    email=models.EmailField(unique=True,null=True)
    p_number=models.IntegerField(null=True)
    adress=models.CharField(max_length=100,blank=True,null=True)
    user_type=models.ForeignKey(user_type,null=True, on_delete=models.SET_NULL)


    region = models.TextField(null=True)

    city = models.TextField(null=True)
    is_verfied=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    EMAIL_FIELD='email'
    @property
    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

class person_type(models.Model):
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type
class lost_P(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    #image=models.FileField(_(""), upload_to=None, max_length=100)
    first_n=models.CharField(max_length=100,null=True,blank=True)
    last_n=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    height=models.IntegerField(null=True,blank=True)
    gender=models.TextField(null=True,blank=True)

    region = models.TextField(null=True,blank=True)

    city = models.TextField(null=True,blank=True)
    cloth=models.TextField(null=True,blank=True)
    mark=models.TextField(null=True,blank=True)
    detail=models.TextField(null=True,blank=True)
    adress=models.CharField(max_length=100,null=True,blank=True)
    p_type=models.ForeignKey(person_type,null=True,on_delete=models.SET_NULL)
    post_date=models.DateTimeField(auto_now_add=True,null=True)
    lost_date=models.DateTimeField(null=True,blank=True)
    update_date=models.DateTimeField(auto_now=True,null=True)
class found_P(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    #image=models.FileField(_(""), upload_to=None, max_length=100)
    first_n=models.CharField(max_length=100,null=True,blank=True)
    last_n=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    height=models.IntegerField(null=True,blank=True)
    gender=models.TextField(null=True,blank=True)

    region = models.TextField(null=True,blank=True)

    city = models.TextField(null=True,blank=True)
    cloth=models.TextField(null=True,blank=True)
    mark=models.TextField(null=True,blank=True)
    detail=models.TextField(null=True,blank=True)
    adress=models.CharField(max_length=100,null=True,blank=True)
    p_type=models.ForeignKey(person_type,null=True,on_delete=models.SET_NULL)
    post_date=models.DateTimeField(auto_now_add=True,null=True)
    lost_date=models.DateTimeField(null=True,blank=True)
    update_date=models.DateTimeField(auto_now=True,null=True)
class wanted_p(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    #image=models.FileField(_(""), upload_to=None, max_length=100)
    first_n=models.CharField(max_length=100,null=True,blank=True)
    last_n=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    height=models.IntegerField(null=True,blank=True)

    region = models.TextField(null=True,blank=True)

    city = models.TextField(null=True,blank=True)

    condition = models.CharField(max_length=100,null=True,blank=True)
    
    post_date=models.DateTimeField(auto_now_add=True,null=True)
    lost_date=models.DateTimeField(null=True,blank=True)
    update_date=models.DateTimeField(auto_now=True,null=True)
    cloth=models.TextField(null=True,blank=True)
    mark=models.TextField(null=True,blank=True)
    detail=models.TextField(null=True,blank=True)
    reason=models.TextField(null=True,blank=True)
    adress=models.CharField(max_length=100,null=True,blank=True)

class matched_p(models.Model):
    found_id=models.ForeignKey(found_P,on_delete=models.SET_NULL,null=True,blank=True)
    lost_id=models.ForeignKey(lost_P,on_delete=models.SET_NULL,null=True,blank=True)
    condition = models.TextField(null=True,blank=True)
class item_type(models.Model):
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type
class found_i(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    #image=models.FileField(_(""), upload_to=None, max_length=100)
    serial_n=models.TextField(null=True,blank=True)
 
    region = models.TextField(null=True,blank=True)

    city = models.TextField(null=True,blank=True)
    detail=models.TextField(null=True,blank=True)
    post_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    adress=models.CharField(max_length=100,null=True,blank=True)
    i_type=models.ForeignKey(item_type,null=True,on_delete=models.SET_NULL)
    lost_date=models.DateTimeField(null=True,blank=True)
    update_date=models.DateTimeField(auto_now=True,null=True,blank=True)
class lost_i(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    #image=models.FileField(_(""), upload_to=None, max_length=100)
    serial_n=models.TextField(null=True,blank=True)
 
    region = models.TextField(null=True,blank=True)

    city = models.TextField(null=True,blank=True)
    detail=models.TextField(null=True,blank=True)
    post_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    adress=models.CharField(max_length=100,null=True,blank=True)
    i_type=models.ForeignKey(item_type,null=True,on_delete=models.SET_NULL)
    lost_date=models.DateTimeField(null=True,blank=True)
    update_date=models.DateTimeField(auto_now=True,null=True,blank=True)
class matched_i(models.Model):
    found_id=models.ForeignKey(found_i,on_delete=models.SET_NULL,null=True)
    lost_id=models.ForeignKey(lost_i,on_delete=models.SET_NULL,null=True)
    condition = models.TextField(null=True,blank=True)