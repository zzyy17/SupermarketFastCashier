# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mobileverifyrecord',
            options={'ordering': ['-send_time'], 'verbose_name': '电话验证码', 'verbose_name_plural': '电话验证码'},
        ),
    ]