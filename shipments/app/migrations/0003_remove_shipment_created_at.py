# Generated by Django 2.2.5 on 2019-09-27 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190927_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='created_at',
        ),
    ]
