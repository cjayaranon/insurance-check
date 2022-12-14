# Generated by Django 3.2.6 on 2021-09-13 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroller', '0012_alter_paymentdetails_payor'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='beneficiary1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='beneficiary1', to='enroller.client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='beneficiary2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='beneficiary2', to='enroller.client'),
            preserve_default=False,
        ),
    ]
