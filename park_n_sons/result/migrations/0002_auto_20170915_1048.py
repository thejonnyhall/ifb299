# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='name',
            field=models.CharField(default='NONE', max_length=50),
        ),
    ]
