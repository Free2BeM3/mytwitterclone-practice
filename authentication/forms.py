from django import forms
from django.forms.widgets import SelectDateWidget
from twitteruser.models import CustomUser


class UserForm(forms.Form):
   first_name = forms.CharField(max_length=25, required=True)
   last_name = forms.CharField(max_length=25, required=True)
   username = forms.CharField(max_length=150, required=True)
   email = forms.EmailField(max_length=100, required=True)
   password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=16, required=True)
   birthday = forms.DateField(widget=SelectDateWidget(years=range(2022, 1930, -1)), required=True)
   avatar = forms.ImageField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

   
