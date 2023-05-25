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
    user_type=models.ForeignKey(user_type,null=True, on_delete=models.SET_NULL,default=3)

    reg = [
        ("AM", "Amhara"),
        ("ORO", "Oromia"),
        ("AA", "Addis Abeba"),
        ("SUMA", "Sumlia"),
    ]
    region = models.CharField(
        choices=reg,
        default="Addis Abeba",
    )
    ci = [
        ("BD", "Bahrdar"),
        ("AD", "Adama"),
        ("AA", "Addis Ababa"),
        ("JJ", "Jigjiga"),
    ]
    city = models.CharField(
        choices=ci,
        default="Addis Ababa",
    )
    is_verfied=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
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
    first_n=models.CharField(max_length=100)
    last_n=models.CharField(max_length=100)
    age=models.IntegerField()
    height=models.IntegerField()
    gender=[
        ("m","male"),
        ("f","female"),
    ]
    reg = [
        ("AM", "Amhara"),
        ("ORO", "Oromia"),
        ("AA", "Addis Abeba"),
        ("SUMA", "Sumlia"),
    ]
    region = models.CharField(
        choices=reg,
        default="Addis Abeba",
    )
    ci= [
        ("BD", "Bahrdar"),
        ("AD", "Adama"),
        ("AA", "Addis Ababa"),
        ("JJ", "Jigjiga"),
    ]
    city = models.CharField(
        choices=ci,
        default="Addis Abeba",
    )
    cloth=models.TextField()
    mark=models.TextField()
    detail=models.TextField()
    adress=models.CharField(max_length=100)
    status=[
        ("h","healthy"),
        ("not_h","Not healthy")
    ]
    p_type=models.ForeignKey(person_type,null=True,on_delete=models.SET_NULL)
    post_date=models.DateTimeField(auto_now_add=True,null=True)
class found_P(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    #image=models.FileField(_(""), upload_to=None, max_length=100)
    first_n=models.CharField(max_length=100)
    last_n=models.CharField(max_length=100)
    age=models.IntegerField()
    height=models.IntegerField()
    reg = [
        ("AM", "Amhara"),
        ("ORO", "Oromia"),
        ("AA", "Addis Abeba"),
        ("SUMA", "Sumlia"),
    ]
    region = models.CharField(
        choices=reg,
        default="Addis Abeba",
    )
    ci= [
        ("BD", "Bahrdar"),
        ("AD", "Adama"),
        ("AA", "Addis Ababa"),
        ("JJ", "Jigjiga"),
    ]
    city = models.CharField(
        choices=ci,
        default="Addis Abeba",
    )
    gender=[
        ("m","male"),
        ("f","female"),
    ]
    cloth=models.TextField()
    mark=models.TextField()
    detail=models.TextField()
    adress=models.CharField(max_length=100)
    status=[
        ("h","healthy"),
        ("not_h","Not healthy")
    ]
    post_date=models.DateTimeField(auto_now_add=True,null=True)
    p_type=models.ForeignKey(person_type,null=True,on_delete=models.SET_NULL)
class wanted_p(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    #image=models.FileField(_(""), upload_to=None, max_length=100)
    first_n=models.CharField(max_length=100)
    last_n=models.CharField(max_length=100)
    age=models.IntegerField()
    height=models.IntegerField()
    reg = [
        ("AM", "Amhara"),
        ("ORO", "Oromia"),
        ("AA", "Addis Abeba"),
        ("SUMA", "Sumlia"),
    ]
    region = models.CharField(
        choices=reg,
        default="Addis Abeba",
    )
    ci= [
        ("BD", "Bahrdar"),
        ("AD", "Adama"),
        ("AA", "Addis Ababa"),
        ("JJ", "Jigjiga"),
    ]
    city = models.CharField(
        choices=ci,
        default="Addis Abeba",
    )
    armed = "armed"
    Not_armed = "not_armed"
    status = [
        (armed, "Armed"),
        (Not_armed, "Not Armed"),
    ]
    condition = models.CharField(
        choices=status,
        default=Not_armed,
    )
    post_date=models.DateTimeField(auto_now_add=True,null=True)
    cloth=models.TextField()
    mark=models.TextField()
    detail=models.TextField()
    reason=models.TextField()
    adress=models.CharField(max_length=100)
    status=[
        ("harm","Harmfull"),
        ("not_harm","Not harmfull")
    ]
class matched_p(models.Model):
    found_id=models.ForeignKey(found_P,on_delete=models.SET_NULL,null=True)
    lost_id=models.ForeignKey(lost_P,on_delete=models.SET_NULL,null=True)
    reg = [
        ("AM", "Amhara"),
        ("ORO", "Oromia"),
        ("AA", "Addis Abeba"),
        ("SUMA", "Sumlia"),
    ]
    region = models.CharField(
        choices=reg,
        default="Addis Abeba",
    )
    ci= [
        ("BD", "Bahrdar"),
        ("AD", "Adama"),
        ("AA", "Addis Ababa"),
        ("JJ", "Jigjiga"),
    ]
    city = models.CharField(
        choices=ci,
        default="Addis Abeba",
    )
    correct = "correct"
    Not_correct = "not_correct"
    status = [
        (correct, "Armed"),
        (Not_correct, "Not Armed"),
    ]
    condition = models.CharField(
        choices=status,
        default=Not_correct,
    )
    post_date=models.DateTimeField(auto_now_add=True,null=True)
class item_type(models.Model):
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.type
class found_i(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    #image=models.FileField(_(""), upload_to=None, max_length=100)
    serial_n=models.TextField()
    reg = [
        ("AM", "Amhara"),
        ("ORO", "Oromia"),
        ("AA", "Addis Abeba"),
        ("SUMA", "Sumlia"),
    ]
    region = models.CharField(
        choices=reg,
        default="Addis Abeba",
    )
    ci= [
        ("BD", "Bahrdar"),
        ("AD", "Adama"),
        ("AA", "Addis Ababa"),
        ("JJ", "Jigjiga"),
    ]
    city = models.CharField(
        choices=ci,
        default="Addis Abeba",
    )
    detail=models.TextField()
    post_date=models.DateTimeField(auto_now_add=True,null=True)
    adress=models.CharField(max_length=100)
    i_type=models.ForeignKey(item_type,null=True,on_delete=models.SET_NULL)
class lost_i(models.Model):
    user=models.ForeignKey(account,null=True,on_delete=models.SET_NULL)
    #image=models.FileField(_(""), upload_to=None, max_length=100)
    reg = [
        ("AM", "Amhara"),
        ("ORO", "Oromia"),
        ("AA", "Addis Abeba"),
        ("SUMA", "Sumlia"),
    ]
    region = models.CharField(
        choices=reg,
        default="Addis Abeba",
    )
    ci= [
        ("BD", "Bahrdar"),
        ("AD", "Adama"),
        ("AA", "Addis Ababa"),
        ("JJ", "Jigjiga"),
    ]
    city = models.CharField(
        choices=ci,
        default="Addis Abeba",
    )
    serial_n=models.TextField()
    detail=models.TextField()
    post_date=models.DateTimeField(auto_now_add=True,null=True)
    adress=models.CharField(max_length=100)
    i_type=models.ForeignKey(item_type,null=True,on_delete=models.SET_NULL)
class matched_i(models.Model):
    found_id=models.ForeignKey(found_i,on_delete=models.SET_NULL,null=True)
    reg = [
        ("AM", "Amhara"),
        ("ORO", "Oromia"),
        ("AA", "Addis Abeba"),
        ("SUMA", "Sumlia"),
    ]
    region = models.CharField(
        choices=reg,
        default="Addis Abeba",
    )
    ci= [
        ("BD", "Bahrdar"),
        ("AD", "Adama"),
        ("AA", "Addis Ababa"),
        ("JJ", "Jigjiga"),
    ]
    city = models.CharField(
        choices=ci,
        default="Addis Abeba",
    )
    lost_id=models.ForeignKey(lost_i,on_delete=models.SET_NULL,null=True)
    correct = "correct"
    Not_correct = "not_correct"
    status = [
        (correct, "Correct match"),
        (Not_correct, "Not Correct Match"),
    ]
    condition = models.CharField(
        choices=status,
        default=Not_correct,
    )
    post_date=models.DateTimeField(auto_now_add=True,null=True)