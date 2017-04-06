# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(
        null=True,
        verbose_name='Descrição'
    )
    qtd = models.IntegerField(
        verbose_name='Quantidade'
    )

    def __unicode__(self):
        return self.nome

