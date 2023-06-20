from django.db import models
from thread.models import account

# Create your models here.
class repo_type(models.Model):
    type=models.CharField(max_length=100)
class repo(models.Model):
    reporter=models.ForeignKey(account, null=True,on_delete=models.SET_NULL,related_name='offended_reporter')
    reported=models.ForeignKey(account,null=True, on_delete=models.SET_NULL,related_name='offender_reported')
    r_type= models.ForeignKey(repo_type,null=True, on_delete=models.SET_NULL)
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
class reponumber(models.Model):
    reported=models.ForeignKey(account,null=True, on_delete=models.SET_NULL,related_name='count_reported')
    repo_n=models.IntegerField(default=0)
    date=models.DateField(auto_now=True)
class reportitemnumber(models.Model):
    reported_item=models.TextField()
    reported_item_n=models.IntegerField(default=0)
    reported_item_type=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)



    
