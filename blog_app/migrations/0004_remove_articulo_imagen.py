# Generated by Django 4.2.1 on 2023-05-22 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='imagen',
        ),
    ]
