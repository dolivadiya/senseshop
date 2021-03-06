# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-18 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flag',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='flag',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='flag',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='flag',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True),
        ),
    ]
