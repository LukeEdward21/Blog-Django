from django import forms as fields_forms
from allauth.account.forms import SignupForm
from django.contrib.auth import forms

from .models import User


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User


class SimpleSignupForm(SignupForm):
    CHOICES = (
        ('F', 'Feminino',),
        ('M', 'Masculino',),
    )

    first_name = fields_forms.CharField(max_length=150)
    last_name = fields_forms.CharField(max_length=150)

    birth_date = fields_forms.DateField(widget=fields_forms.TextInput(attrs={'type': 'date'}))
    gender = fields_forms.ChoiceField(widget=fields_forms.RadioSelect, choices=CHOICES)

    
    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.birth_date = self.cleaned_data['birth_date']
        user.gender = self.cleaned_data['gender']
        user.save()
        return user
