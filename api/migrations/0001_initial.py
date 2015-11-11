# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
                ('catalogID', models.CharField(max_length=7)),
                ('itemId', models.CharField(unique=True, max_length=11)),
                ('discountCode', models.CharField(max_length=3)),
                ('categoryCode', models.CharField(max_length=3)),
                ('orderDate', models.CharField(max_length=11)),
                ('sellDate', models.CharField(max_length=11)),
                ('qty', models.IntegerField(default=0)),
                ('page', models.CharField(max_length=5)),
                ('reoccuring', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='monthlyorder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('qty', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='previewselections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=7)),
            ],
        ),
    ]
