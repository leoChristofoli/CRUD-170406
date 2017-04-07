# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from oper import models as oper_models


class ProdutoList(ListView):
    model = oper_models.Produto


class ProdutoCreate(CreateView):
    model = oper_models.Produto
    success_url = reverse_lazy('produto_add')
    fields = ['nome', 'descricao', 'qtd']

    def get_success_url(self):
        return reverse_lazy('produto_list')

    def dispatch(self, *args, **kwargs):
        return super(ProdutoCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return super(ProdutoCreate, self).form_valid(form)


class ProdutoUpdate(UpdateView):
    model = oper_models.Produto
    success_url = reverse_lazy('produto_add')
    fields = ['nome', 'descricao', 'qtd']

    def get_success_url(self):
        return reverse_lazy('produto_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.updated_by = self.request.user
        obj.save()
        return super(ProdutoUpdate, self).form_valid(form)


class ProdutoDelete(DeleteView):
    model = oper_models.Produto
    success_url = reverse_lazy('produto_list')
