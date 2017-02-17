# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 06:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verify_number',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
