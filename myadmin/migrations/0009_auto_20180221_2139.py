# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-21 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_auto_20180218_2217'),
        ('myadmin', '0008_auto_20180221_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='email',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='mobile',
        ),
        migrations.AddField(
            model_name='complaint',
            name='c_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='login.customer'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='replay',
            field=models.CharField(default='a', max_length=1000),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='cm_msg',
            field=models.CharField(default='a', max_length=1000),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='c_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='login.customer'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='c_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='login.customer'),
        ),
        migrations.AlterField(
            model_name='temp_cart',
            name='c_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='login.customer'),
        ),
    ]
