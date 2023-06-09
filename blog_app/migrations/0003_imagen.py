# Generated by Django 4.2.1 on 2023-05-22 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_articulo_fecha_alter_articulo_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='blog_app.articulo')),
            ],
        ),
    ]
