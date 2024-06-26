# Generated by Django 4.1 on 2024-05-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('celular', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=128)),
                ('habilitado', models.BooleanField(default=True)),
                ('fechaAlta', models.DateTimeField(auto_now_add=True)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
    ]
