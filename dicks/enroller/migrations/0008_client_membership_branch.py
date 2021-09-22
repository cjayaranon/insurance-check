# Generated by Django 3.2.6 on 2021-09-03 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroller', '0007_clienttagging_cutoffperiod_paymentdetails_paymenttype_premiumamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='membership_branch',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='enroller.branch'),
            preserve_default=False,
        ),
    ]