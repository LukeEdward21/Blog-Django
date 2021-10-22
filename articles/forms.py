from django import forms

from .models import Article


class WriteForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = (
            'slug', 
            'title', 
            'thumbnail', 
            'resume', 
            'body', 
            'author'
            ) 
