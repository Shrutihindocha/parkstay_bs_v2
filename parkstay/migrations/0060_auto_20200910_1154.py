# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-09-10 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0059_booking_do_not_send_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='do_not_send_invoice',
            field=models.BooleanField(default=False),
        ),
    ]
