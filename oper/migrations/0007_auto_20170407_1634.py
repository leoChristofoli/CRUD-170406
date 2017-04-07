# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oper', '0006_deletedproduto'),
    ]

    operations = [
        migrations.AddField(
            model_name='deletedproduto',
            name='when_deleted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='deletedproduto',
            name='when_created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='deletedproduto',
            name='when_updated',
            field=models.DateTimeField(null=True),
        ),
    ]
