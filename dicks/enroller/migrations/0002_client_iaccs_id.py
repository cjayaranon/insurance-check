# Generated by Django 3.2.6 on 2021-08-24 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='iaccs_id',
            field=models.IntegerField(default=0),
        ),
    ]
