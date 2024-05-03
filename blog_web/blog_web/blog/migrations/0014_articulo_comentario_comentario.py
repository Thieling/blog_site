# Generated by Django 5.0.3 on 2024-05-03 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_avatar_delete_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='comentario',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id_comentario', models.AutoField(primary_key=True, serialize=False)),
                ('nom_usr', models.CharField(max_length=10)),
                ('contenido', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('activo', models.BooleanField(default=False)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='blog.articulo')),
            ],
        ),
    ]
