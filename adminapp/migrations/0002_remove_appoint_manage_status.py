# Generated by Django 5.0.4 on 2024-05-10 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoint_manage',
            name='status',
        ),
    ]
