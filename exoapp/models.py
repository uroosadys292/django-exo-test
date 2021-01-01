from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)