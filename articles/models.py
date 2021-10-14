from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from uuid import uuid4
import os


def path_and_rename(instance, filename):
    upload_to = 'thumbnails/'
    ext = filename.split('.')[-1]
    
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class Article(models.Model):
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    title = models.CharField('Título', max_length=150, unique=True)
    thumbnail = models.ImageField('Thumbnail', upload_to=path_and_rename, blank=True)
    resume = models.CharField('Resumo', max_length=150)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'is_writer': True},
        verbose_name='Autor',
        )
    body = models.TextField('Texto')
    created = models.DateTimeField('Criado', auto_now_add=True)
    updated = models.DateTimeField('Atualizado', auto_now=True)

    class Meta:
        ordering = ("-created",)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug": self.slug})
    
