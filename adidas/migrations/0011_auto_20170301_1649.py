# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adidas', '0010_auto_20170301_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='teams',
            field=models.ManyToManyField(null=True, to='adidas.Team', verbose_name='Squadre iscritte'),
        ),
    ]