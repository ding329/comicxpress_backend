# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import comicxpress_backend.api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151113_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='catalogId',
            new_name='catalogid',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='categoryCode',
            new_name='categorycode',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='discountCode',
            new_name='discountcode',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='itemId',
            new_name='itemid',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='orderDate',
            new_name='orderdate',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='sellDate',
            new_name='selldate',
        ),
        migrations.AlterField(
            model_name='catalog',
            name='name',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='monthlyorder',
            name='name',
            field=models.CharField(max_length=75, validators=[comicxpress_backend.api.validators.removeJavascriptKeyword]),
        ),
    ]
