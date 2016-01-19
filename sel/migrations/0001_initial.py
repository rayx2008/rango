# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('creator', models.TextField()),
                ('bill_of_lading_no', models.TextField()),
                ('plan_wt', models.DecimalField(decimal_places=3, max_digits=10, verbose_name=0)),
                ('finish_wt', models.DecimalField(decimal_places=3, max_digits=10, verbose_name=0)),
                ('balance_user_name', models.TextField()),
            ],
        ),
    ]