# Generated by Django 4.0.3 on 2022-05-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_rename_miaou_marque_marque_rename_miaou_type_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdd',
            name='Type',
            field=models.CharField(max_length=100),
        ),
    ]
