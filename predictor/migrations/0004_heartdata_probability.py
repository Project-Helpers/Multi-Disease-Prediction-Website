# Generated by Django 3.1.4 on 2021-04-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0003_heartdata_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='heartdata',
            name='probability',
            field=models.FloatField(null=True),
        ),
    ]