from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SEX_CHOICES = (
        ('F', 'Feminino',),
        ('M', 'Masculino',),
    )
    first_name = models.CharField('Nome', max_length=150)
    last_name = models.CharField('Sobrenome', max_length=150)
    email = models.EmailField('E-mail', unique=True, max_length=150)


    birth_date = models.DateField('Data de nascimento', auto_now_add=True)
    gender = models.CharField('Gênero',
        max_length=1,
        choices=SEX_CHOICES,
    )
    image = models.ImageField('Foto', upload_to='users/', blank=True)

    is_writer = models.BooleanField('Escritor', default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'birth_date', 'gender']
