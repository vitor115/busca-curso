# Generated by Django 3.2.6 on 2021-08-12 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscacurso', '0005_auto_20210811_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='college_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
