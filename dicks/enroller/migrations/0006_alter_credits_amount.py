# Generated by Django 3.2.6 on 2021-08-24 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroller', '0005_alter_client_name_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credits',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]