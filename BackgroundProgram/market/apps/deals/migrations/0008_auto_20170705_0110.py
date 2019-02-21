# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 01:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deals', '0007_auto_20170704_2112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customers',
            options={'ordering': ['-add_time'], 'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterModelOptions(
            name='mobileverf',
            options={'ordering': ['-add_time'], 'verbose_name': '手机验证码', 'verbose_name_plural': '手机验证码'},
        ),
        migrations.AddField(
            model_name='customers',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]