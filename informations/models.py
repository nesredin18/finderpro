from django.db import models
from thread.models import account

# Create your models here.
class about(models.Model):
    about_detail=models.TextField(null=True,blank=True,default='about')
class region(models.Model):
    region_name=models.CharField(max_length=100,null=True,blank=True,default='region')
class city(models.Model):
    region=models.ForeignKey(region,null=True, on_delete=models.SET_NULL)
    city=models.CharField(max_length=100,null=True,blank=True,default='city')
class contact_us(models.Model):
    address=models.CharField(max_length=100,null=True,blank=True,default='address')
    phone=models.CharField(max_length=100,null=True,blank=True,default='phone')
    email=models.EmailField(max_length=100,null=True,blank=True,default='email')
    facebook=models.CharField(max_length=100,null=True,blank=True,default='facebook')
    twitter=models.CharField(max_length=100,null=True,blank=True,default='twitter')
    instagram=models.CharField(max_length=100,null=True,blank=True,default='instagram')
    youtube=models.CharField(max_length=100,null=True,blank=True,default='youtube')
class help(models.Model):
    help_detail=models.TextField(null=True,blank=True,default='help')
class privacy(models.Model):
    privacy_detail=models.TextField(null=True,blank=True,default='privacy')
class terms(models.Model):
    terms_detail=models.TextField(null=True,blank=True,default='terms')
class faq(models.Model):
    question=models.TextField(null=True,blank=True,default='question')
    answer=models.TextField(null=True,blank=True,default='answer')
    asker=models.ForeignKey(account,null=True, on_delete=models.SET_NULL,related_name='asker')
class contact(models.Model):
    question=models.TextField(null=True,blank=True,default='question')
    asker=models.EmailField(max_length=100,null=True,blank=True,default='email')
    answer=models.TextField(null=True,blank=True,default='answer')
    answerer=models.ForeignKey(account,null=True, on_delete=models.SET_NULL,related_name='answerer')
    

