# Generated by Django 2.0.10 on 2019-02-26 15:18

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
    ]
