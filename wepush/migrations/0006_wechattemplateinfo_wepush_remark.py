# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 02:42
from __future__ import unicode_literals

from django.db import migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wepush', '0005_wechattemplateinfo_token_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='wechattemplateinfo',
            name='wepush_remark',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, help_text='\u6a21\u677f\u6d88\u606f\u5907\u6ce8', max_length=22, null=True),
        ),
    ]