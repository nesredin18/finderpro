from django.db import models
from thread.models import account

# Create your models here.
class repo_type(models.Model):
    type=models.CharField(max_length=100)
class repo(models.Model):
    reporter=models.ForeignKey(account, null=True,on_delete=models.SET_NULL,related_name='reporter')
    reported=models.ForeignKey(account,null=True, on_delete=models.SET_NULL,related_name='reported')
    r_type= models.ForeignKey(repo_type,null=True, on_delete=models.SET_NULL)
    content=models.TextField()
    repo_n=models.IntegerField()
    date=models.DateField(auto_now=True)


    
