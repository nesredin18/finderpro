from django.db import models
from thread.models import account

# Create your models here.
class notify(models.Model):
    sender=models.ForeignKey(account, null=True,on_delete=models.SET_NULL,related_name='notif_sender',blank=True)
    rec=models.ForeignKey(account,null=True, on_delete=models.SET_NULL,related_name='notif_reciever')
    content=models.TextField()
    date=models.DateField(auto_now=True)

