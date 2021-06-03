from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='profile_pics/')
    is_online = models.BooleanField(default=False)
    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
    

    