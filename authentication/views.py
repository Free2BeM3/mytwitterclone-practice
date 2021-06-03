from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from authentication.forms import UserForm, LoginForm
from twitteruser.models import CustomUser
from tweet.models import Tweet

# Create your views here.


def index(request):
   if request.user.is_authenticated:
        users = CustomUser.objects.all()[::-1]
        posts = Tweet.objects.all()[::-1]
        return render(request, 'index.html', {'users': users, 'posts': posts})
   else:
        return HttpResponseRedirect(reverse('login'))



def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            newuser = CustomUser.objects.create_user(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                email=data['email'],
                password=data['password'],
                birthday=data['birthday'],
                avatar=data['avatar'],
            )
            
            return HttpResponseRedirect(reverse('login'))

    form = UserForm()
    return render(request, 'signupform.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                print(type(user))
                user.is_online = True
                user.save()
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))



    form = LoginForm()
    return render(request, 'login_form.html', {'form': form})



def logout_view(request):
    CustomUser.objects.filter(username=request.user).update(
        is_online=False
    )
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))