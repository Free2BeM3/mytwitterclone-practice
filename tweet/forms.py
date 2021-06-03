from django import forms
from tweet.models import Tweet


class TweetForm(forms.Form):

    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)