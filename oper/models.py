# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(
        null=True,
        verbose_name='Descrição'
    )
    qtd = models.IntegerField(
        verbose_name='Quantidade'
    )
    when_created = models.DateTimeField(null=True, auto_now_add=True)
    when_updated = models.DateTimeField(null=True, auto_now=True)
    created_by = models.ForeignKey(User, null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='produto_updated')

    def __unicode__(self):
        return self.nome

