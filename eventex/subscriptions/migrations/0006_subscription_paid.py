# Generated by Django 2.0.10 on 2019-02-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_remove_uuid_null_20190214_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
