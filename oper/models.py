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
    client_ip = models.GenericIPAddressField(null=True)

    def __unicode__(self):
        return self.nome


class DeletedProduto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(
        null=True,
        verbose_name='Descrição'
    )
    qtd = models.IntegerField(
        verbose_name='Quantidade'
    )
    when_created = models.DateTimeField(null=True)
    when_updated = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='produto_del')
    client_ip = models.GenericIPAddressField(null=True)
    when_deleted = models.DateTimeField(null=True, auto_now_add=True)
    deleted_by = models.ForeignKey(User, null=True, related_name='deleted_produto')

    def __unicode__(self):
        return self.nome
