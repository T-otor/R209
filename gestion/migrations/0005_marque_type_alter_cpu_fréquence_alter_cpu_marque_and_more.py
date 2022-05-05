# Generated by Django 4.0.3 on 2022-05-05 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_hdd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miaou', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miaou', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='cpu',
            name='Fréquence',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='Marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.marque'),
        ),
        migrations.AlterField(
            model_name='hdd',
            name='Marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.marque'),
        ),
        migrations.AlterField(
            model_name='hdd',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.type'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='Marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.marque'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.type'),
        ),
    ]
