# Generated by Django 5.0.3 on 2024-04-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino')], default='---', max_length=12),
        ),
    ]
