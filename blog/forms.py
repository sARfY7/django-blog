from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    tags = forms.CharField()
