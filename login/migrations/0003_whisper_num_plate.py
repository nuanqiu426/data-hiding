# Generated by Django 3.1.2 on 2020-11-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20201116_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='whisper',
            name='Num_plate',
            field=models.IntegerField(default=446146024, max_length=20),
        ),
    ]