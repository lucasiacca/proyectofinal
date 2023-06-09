# Generated by Django 4.2.1 on 2023-05-21 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=200)),
                ('cuerpo', models.TextField()),
                ('seccion', models.CharField(choices=[('Policiales', 'Policiales'), ('Deportes', 'Deportes'), ('Politica', 'Politica'), ('Interes General', 'Interes General')], max_length=1028)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to='imagenes/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
