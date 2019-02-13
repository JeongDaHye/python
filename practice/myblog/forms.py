from django import forms
from .models import Myblog

class BlogPost(forms.ModelForm):
  class Meta:
    model = Myblog
    fields = ['title', 'body']
    #email = forms.EmailField()
    #files = forms.FilePathField()
    #url = forms.URLField()
    #words = forms.CharField(max_length=200)
    #max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])
