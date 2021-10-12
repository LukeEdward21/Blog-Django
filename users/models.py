from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField('Nome', max_length=150)
    last_name = models.CharField('Sobrenome', max_length=150)
    email = models.EmailField('E-mail', unique=True)
    image = models.ImageField('Foto', upload_to='users/', blank=True)
    is_writer = models.BooleanField('Escritor', default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
