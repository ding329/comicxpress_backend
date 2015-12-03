# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import comicxpress_backend.api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151126_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='catalogid',
            field=models.IntegerField(validators=[comicxpress_backend.api.validators.validateInterger]),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='qty',
            field=models.IntegerField(default=0, validators=[comicxpress_backend.api.validators.validateInterger]),
        ),
        migrations.AlterField(
            model_name='monthlyorder',
            name='name',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='monthlyorder',
            name='qty',
            field=models.IntegerField(default=0, validators=[comicxpress_backend.api.validators.validateInterger]),
        ),
    ]
