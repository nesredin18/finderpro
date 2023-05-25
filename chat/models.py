from django.db import models
from thread.models import account

# Create your models here.
class message(models.Model):
    sender=models.ForeignKey(account, null=True,on_delete=models.SET_NULL,related_name='sender')
    rec=models.ForeignKey(account,null=True, on_delete=models.SET_NULL,related_name='reciever')
    content=models.TextField()
    date=models.DateField(auto_now=True)

