from django import forms as fields_forms
from allauth.account.forms import SignupForm, LoginForm
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

    first_name = fields_forms.CharField(max_length=150, widget=fields_forms.TextInput(attrs={'placeholder': 'Nome'}))
    last_name = fields_forms.CharField(max_length=150, widget=fields_forms.TextInput(attrs={'placeholder': 'Sobrenome'}))

    birth_date = fields_forms.DateField(widget=fields_forms.TextInput(attrs={'type': 'date'}), help_text='Data de nascimento.')
    gender = fields_forms.ChoiceField(widget=fields_forms.RadioSelect, choices=CHOICES)

    
    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        # user.username = self.cleaned_data['username']
        # user.username = user.username.lower()

        user.birth_date = self.cleaned_data['birth_date']
        user.gender = self.cleaned_data['gender']
        # user.is_active = False
        user.save()
        
        return user
    
    def __init__(self, *args, **kwargs):
        super(SimpleSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ""
        self.fields['username'].label = ""
        self.fields['first_name'].label = ""
        self.fields['last_name'].label = ""
        self.fields['birth_date'].label = ""
        self.fields['gender'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""
    
    field_order = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'birth_date', 'gender']


class SimpleLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(SimpleLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].label = ""
        self.fields['password'].label = ""

