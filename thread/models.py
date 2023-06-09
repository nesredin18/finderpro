from django.db import models
from django.contrib.auth.models import AbstractUser
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
def uploadlosti_to(instance, filename):
    return 'images/lostitem{filename}'.format(filename=filename)
def upload_to(instance, filename):
    return 'images/lostperson{filename}'.format(filename=filename)
def uploadfoundi_to(instance, filename):
    return 'images/founditem{filename}'.format(filename=filename)
def uploadfoundp_to(instance, filename):
    return 'images/foundperson{filename}'.format(filename=filename)
def uploadaccount_to(instance, filename):
    return 'images/account{filename}'.format(filename=filename)
def uploadwantedp_to(instance, filename):
    return 'images/wantedp{filename}'.format(filename=filename)
class user_type(models.Model):
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type
class account(AbstractUser):
    email=models.EmailField(unique=True,null=True)
    image_url = models.ImageField(upload_to=uploadaccount_to, blank=True, null=True)
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
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    height=models.IntegerField(null=True,blank=True)
    gender=models.TextField(null=True,blank=True)

    region = models.TextField(null=True,blank=True)
    post_type=models.CharField(max_length=100,null=True,blank=True,default="lost person")
    city = models.TextField(null=True,blank=True)
    cloth=models.TextField(null=True,blank=True)
    mark=models.TextField(null=True,blank=True)
    detail=models.TextField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    p_type=models.ForeignKey(person_type,null=True,on_delete=models.SET_NULL)
    post_date=models.DateTimeField(auto_now_add=True,null=True)
    lost_date=models.DateTimeField(null=True,blank=True)
    update_date=models.DateTimeField(auto_now=True,null=True)
class found_P(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    image_url = models.ImageField(upload_to=uploadfoundp_to, blank=True, null=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    height=models.IntegerField(null=True,blank=True)
    gender=models.TextField(null=True,blank=True)

    region = models.TextField(null=True,blank=True)
    post_type=models.CharField(max_length=100,null=True,blank=True,default="found-person")

    city = models.TextField(null=True,blank=True)
    cloth=models.TextField(null=True,blank=True)
    mark=models.TextField(null=True,blank=True)
    detail=models.TextField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    p_type=models.ForeignKey(person_type,null=True,on_delete=models.SET_NULL)
    post_date=models.DateTimeField(auto_now_add=True,null=True)
    lost_date=models.DateTimeField(null=True,blank=True)
    update_date=models.DateTimeField(auto_now=True,null=True)
class wanted_p(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    image_url = models.ImageField(upload_to=uploadwantedp_to, blank=True, null=True)
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


class item_type(models.Model):
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type
class found_i(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    image_url = models.ImageField(upload_to=uploadfoundi_to, blank=True, null=True)
    serial_n=models.TextField(null=True,blank=True)
    post_type=models.CharField(max_length=100,null=True,blank=True,default="found-item")

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
    image_url = models.ImageField(upload_to=uploadlosti_to, blank=True, null=True)
    serial_n=models.TextField(null=True,blank=True)
 
    region = models.TextField(null=True,blank=True)
    post_type=models.CharField(max_length=100,null=True,blank=True,default="lost item")

    city = models.TextField(null=True,blank=True)
    detail=models.TextField(null=True,blank=True)
    post_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    adress=models.CharField(max_length=100,null=True,blank=True)
    i_type=models.ForeignKey(item_type,null=True,on_delete=models.SET_NULL)
    lost_date=models.DateTimeField(null=True,blank=True)
    update_date=models.DateTimeField(auto_now=True,null=True,blank=True)
