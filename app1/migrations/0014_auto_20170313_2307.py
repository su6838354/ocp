# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_activity2tag_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity2tag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
