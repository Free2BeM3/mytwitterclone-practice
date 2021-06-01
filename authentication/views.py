from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from authentication.forms import UserForm, LoginForm
from twitteruser.models import CustomUser
from tweet.models import Tweet

# Create your views here.


def index(request):
   if request.user.is_authenticated:
        users = CustomUser.objects.all()
        posts = Tweet.objects.all()
        return render(request, 'index.html', {'users': users, 'posts': posts})
   else:
        return HttpResponseRedirect(reverse('login'))



def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newuser = CustomUser.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = UserForm()
    return render(request, 'generic_form.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))



    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))