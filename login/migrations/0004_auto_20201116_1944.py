# Generated by Django 3.1.2 on 2020-11-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_whisper_num_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whisper',
            name='Num_plate',
            field=models.IntegerField(default=446146024),
        ),
    ]
