from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserData(AbstractUser):
    name=models.TextField(verbose_name='Name')

