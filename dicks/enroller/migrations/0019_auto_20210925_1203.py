# Generated by Django 3.2.6 on 2021-09-25 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroller', '0018_agent_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='enroller.branch'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='enroller.designation'),
        ),
    ]