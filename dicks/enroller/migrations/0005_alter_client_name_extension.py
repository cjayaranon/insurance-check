# Generated by Django 3.2.6 on 2021-08-24 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroller', '0004_alter_client_civil_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name_extension',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
