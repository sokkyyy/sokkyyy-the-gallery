# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-11-07 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20191107_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('travel', 'Travel'), ('food', 'Food'), ('places', 'Places'), ('people', 'People'), ('sports', 'Sports')], max_length=20),
        ),
    ]
