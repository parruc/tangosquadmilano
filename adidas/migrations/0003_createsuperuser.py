# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 10:57
from __future__ import unicode_literals
from django.contrib.auth.hashers import make_password
from django.db import migrations


def forwards(apps, schema_editor):
     User = apps.get_registered_model('auth', 'User')
     admin = User(
         username='admin',
         email='parruc@gmail.com',
         password=make_password('admin'),
         is_superuser=True,
         is_staff=True
     )
     admin.save()


class Migration(migrations.Migration):

    dependencies = [
        ('adidas', '0002_auto_20170209_1005'),
    ]

    operations = [migrations.RunPython(forwards),
    ]
