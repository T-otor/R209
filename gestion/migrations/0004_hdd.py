# Generated by Django 4.0.3 on 2022-05-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_cpu'),
    ]

    operations = [
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marque', models.CharField(max_length=100)),
                ('Modèle', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=4)),
                ('Espace', models.CharField(max_length=40)),
                ('SN', models.CharField(max_length=20)),
            ],
        ),
    ]