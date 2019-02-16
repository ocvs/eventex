# Generated by Django 2.0.10 on 2019-02-14 18:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_populate_uuid_values_20190214_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='masked_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='masked_id'),
        ),
    ]
