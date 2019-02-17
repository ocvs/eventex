# Generated by Django 2.0.10 on 2019-02-14 18:10

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    mymodel = apps.get_model('subscriptions', 'Subscription')
    for row in mymodel.objects.all():
        row.masked_id = uuid.uuid4()
        row.save(update_fields=['masked_id'])


class Migration(migrations.Migration):
    dependencies = [
        ('subscriptions', '0003_subscription_masked_id'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]