# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-04 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_dt', models.DateField()),
                ('episode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
                ('remark', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Master'),
        ),
    ]
