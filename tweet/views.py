from django.shortcuts import render,HttpResponseRedirect, reverse

from tweet.models import Tweet
from tweet.forms import TweetForm
# Create your views here.


def add_tweet(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TweetForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_tweet = Tweet.objects.create(
                    title=data['title'],
                    body=data['body'],
                    created_by=request.user,
                )
            
                return HttpResponseRedirect(reverse('homepage'))

        form = TweetForm()
        return render(request, 'addtweetform.html', {'form': form})

    else:
        return HttpResponseRedirect(reverse('login'))