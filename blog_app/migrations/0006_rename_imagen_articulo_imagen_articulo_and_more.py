# Generated by Django 4.2.1 on 2023-05-22 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_articulo_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='imagen',
            new_name='imagen_articulo',
        ),
        migrations.RenameField(
            model_name='imagen',
            old_name='imagen',
            new_name='imagen_articulo',
        ),
        migrations.AlterField(
            model_name='imagen',
            name='articulo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_app.articulo'),
        ),
    ]
