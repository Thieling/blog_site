# Generated by Django 5.0.3 on 2024-04-29 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_usuario_genero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='nom_usr',
            new_name='usuario',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino')], max_length=12),
        ),
    ]