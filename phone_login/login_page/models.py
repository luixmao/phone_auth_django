from __future__ import unicode_literals
import re

from django.db import models
from django.contrib.auth.models import User

class User_phone_number(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100, unique=True)


class Verify_number(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=100, unique=True)
    verification_code =models.CharField(max_length=30)
    is_verified =models.BooleanField(default=False)
    user = models.ForeignKey(User,blank=True,null=True )
