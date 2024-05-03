# Generated by Django 5.0.3 on 2024-04-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_nom_usr_usuario_usuario_alter_usuario_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('nom_usr', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('comentario', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='articulo',
            name='comentario',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]