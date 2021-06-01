from django import forms
from twitteruser.models import CustomUser

class UserForm(forms.Form):

   username = forms.CharField(max_length=150)
   email = forms.EmailField()
   password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

   