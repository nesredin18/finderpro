from django.db import models
from thread.models import account,lost_i,lost_P,found_P,found_i

# Create your models here.
class notify(models.Model):
    rec=models.ForeignKey(account,null=True, on_delete=models.SET_NULL,related_name='notif_reciever_matcher')
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
class matched_p(models.Model):
    found_id=models.ForeignKey(found_P,on_delete=models.SET_NULL,null=True,blank=True)
    lost_id=models.ForeignKey(lost_P,on_delete=models.SET_NULL,null=True,blank=True)
    condition = models.TextField(null=True,blank=True,default="accurate")
class matched_i(models.Model):
    found_id=models.ForeignKey(found_i,on_delete=models.SET_NULL,null=True)
    lost_id=models.ForeignKey(lost_i,on_delete=models.SET_NULL,null=True)
    condition = models.TextField(null=True,blank=True,default="accurate")