# Generated by Django 3.2.7 on 2021-10-24 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail_credits',
            field=models.CharField(blank=True, max_length=150, verbose_name='Autor da imagem'),
        ),
    ]
