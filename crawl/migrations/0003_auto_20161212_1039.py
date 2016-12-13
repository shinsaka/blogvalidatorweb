# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0002_imageassessment_crawl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=1000, null=True)),
                ('violence', models.CharField(max_length=200, null=True)),
                ('adult', models.CharField(max_length=200, null=True)),
                ('spoof', models.CharField(max_length=200, null=True)),
                ('medical', models.CharField(max_length=200, null=True)),
                ('page_title', models.CharField(max_length=1000, null=True)),
                ('page_url', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='imageassessment',
            name='crawl',
        ),
        migrations.DeleteModel(
            name='Crawl',
        ),
        migrations.DeleteModel(
            name='ImageAssessment',
        ),
    ]
