# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oper', '0009_auto_20170408_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='qtd',
            field=models.PositiveIntegerField(verbose_name='Quantidade'),
        ),
    ]
