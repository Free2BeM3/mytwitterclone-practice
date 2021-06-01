from django.db import models
from twitteruser.models import CustomUser
# Create your models here.
class Tweet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=140)
    created_by = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)