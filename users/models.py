
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4
import os


def path_and_rename(instance, filename):
    upload_to = 'users/'
    ext = filename.split('.')[-1]
    
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class User(AbstractUser):
    SEX_CHOICES = (
        ('F', 'Feminino',),
        ('M', 'Masculino',),
    )


    first_name = models.CharField('Nome', max_length=150)
    last_name = models.CharField('Sobrenome', max_length=150)
    email = models.EmailField('E-mail', unique=True, max_length=150)
    username = models.CharField('Nome de usuário', unique=True, max_length=150)

    # slug = models.SlugField('Slug', unique=True, max_length=150)


    birth_date = models.DateField('Data de nascimento', auto_now_add=True)
    gender = models.CharField(
        'Gênero',
        max_length=1,
        choices=SEX_CHOICES,
    )
    image = models.ImageField('Foto', upload_to=path_and_rename, blank=True)

    is_writer = models.BooleanField('Escritor', default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'birth_date', 'gender']




