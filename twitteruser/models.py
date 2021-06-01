from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ManyToManyField

# Create your models here.


class CustomUser(AbstractUser):
    ...
    

    