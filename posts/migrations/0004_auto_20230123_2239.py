# Generated by Django 3.2.5 on 2023-01-24 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230123_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='descricao_curta',
        ),
        migrations.RemoveField(
            model_name='post',
            name='descricao_longa',
        ),
        migrations.AddField(
            model_name='post',
            name='descricao',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
