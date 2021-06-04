from typing import Any
from django.contrib.auth import get_user
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contacts(models.Model):
    phone_number = models.CharField(max_length=7)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relation = models.CharField(default='no relation', max_length=100)

    def __str__(self):
        return self.first_name+' '+self.last_name