# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oper', '0004_produto_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='client_ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
