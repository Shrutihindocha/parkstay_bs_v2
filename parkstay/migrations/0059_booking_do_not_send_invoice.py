# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-09-10 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0058_booking_property_cache_stale'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='do_not_send_invoice',
            field=models.BooleanField(default=True),
        ),
    ]
