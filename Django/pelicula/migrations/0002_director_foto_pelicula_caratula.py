# Generated by Django 4.1.5 on 2023-01-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='foto',
            field=models.URLField(blank=True, default='DEFAULT VALUE', max_length=540, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='caratula',
            field=models.URLField(blank=True, default='DEFAULT VALUE', max_length=540, null=True),
        ),
    ]
