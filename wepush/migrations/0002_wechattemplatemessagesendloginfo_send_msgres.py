# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wepush', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wechattemplatemessagesendloginfo',
            name='send_msgres',
            field=models.TextField(blank=True, help_text='\u53d1\u9001\u56de\u6267', null=True, verbose_name='send_msgres'),
        ),
    ]
