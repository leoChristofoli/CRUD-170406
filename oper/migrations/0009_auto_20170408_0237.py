# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oper', '0008_deletedproduto_deleted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletedproduto',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='deletedproduto',
            name='qtd',
            field=models.IntegerField(null=True, verbose_name='Quantidade'),
        ),
    ]
