# Generated by Django 3.2.6 on 2021-10-12 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroller', '0017_alter_agent_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='designation',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='enroller.designation'),
        ),
    ]