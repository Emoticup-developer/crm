from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LogsAndHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.TextField(blank=True,null=True)
    method = models.TextField(blank=True,null=True)
    device = models.TextField(blank=True,null=True)
    ip = models.TextField(blank=True,null=True)
    meta = models.TextField(blank=True,null=True)
    
    
    def __str__(self):
        return str(self.location) + str(self.user)