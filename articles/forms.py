from django import forms

from .models import Article


class WriteForm(forms.ModelForm):
    # author = forms.ModelChoiceField(choices)
    class Meta:
        model = Article
        fields = (
            'slug', 
            'title', 
            'thumbnail', 
            'resume', 
            'body', 
            # 'author'
            ) 
