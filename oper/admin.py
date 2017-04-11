# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from oper.models import Produto, DeletedProduto

admin.site.register(Produto)
admin.site.register(DeletedProduto)
