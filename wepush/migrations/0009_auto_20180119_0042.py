# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wepush', '0008_wechattemplatereceiverinfo_receiver_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wechattemplateinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Create Time', verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='wechattemplateinfo',
            name='status',
            field=models.BooleanField(db_index=True, default=True, help_text='Status', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='wechattemplateinfo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Update Time', verbose_name='updated_at'),
        ),
        migrations.AlterField(
            model_name='wechattemplatemessagerequestloginfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Create Time', verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='wechattemplatemessagerequestloginfo',
            name='status',
            field=models.BooleanField(db_index=True, default=True, help_text='Status', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='wechattemplatemessagerequestloginfo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Update Time', verbose_name='updated_at'),
        ),
        migrations.AlterField(
            model_name='wechattemplatemessagesendloginfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Create Time', verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='wechattemplatemessagesendloginfo',
            name='status',
            field=models.BooleanField(db_index=True, default=True, help_text='Status', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='wechattemplatemessagesendloginfo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Update Time', verbose_name='updated_at'),
        ),
        migrations.AlterField(
            model_name='wechattemplatereceiverinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Create Time', verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='wechattemplatereceiverinfo',
            name='status',
            field=models.BooleanField(db_index=True, default=True, help_text='Status', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='wechattemplatereceiverinfo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Update Time', verbose_name='updated_at'),
        ),
    ]