# Generated by Django 5.0.3 on 2024-04-30 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_comentario_comentario_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='id_comentario',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nom_usr',
            field=models.CharField(max_length=10),
        ),
    ]