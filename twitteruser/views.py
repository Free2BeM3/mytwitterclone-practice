from django.shortcuts import render
from .models import CustomUser
from tweet.models import Tweet
# Create your views here.

def profile_view(request, user_id: int):
    current_user = CustomUser.objects.get(id=user_id)
    my_tweets = Tweet.objects.filter(created_by=current_user)[::-1]
    return render(request, 'profile.html', {'user': current_user, 'posts': my_tweets})
