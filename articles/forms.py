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
            'thumbnail_credits',
            'type',
            'resume', 
            'body', 
            # 'author'
            'is_exclusive',
            ) 
