# Generated by Django 5.0.3 on 2024-04-30 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comentario_activo_comentario_articulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='comentario',
            new_name='contenido',
        ),
    ]