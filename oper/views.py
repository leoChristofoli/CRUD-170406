# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from oper import models as oper_models


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ProdutoList(ListView):
    model = oper_models.Produto


class ProdutoCreate(CreateView):
    model = oper_models.Produto
    success_url = reverse_lazy('produto_list')
    fields = ['nome', 'descricao', 'qtd']

    def dispatch(self, *args, **kwargs):
        return super(ProdutoCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.client_ip = get_ip(self.request)
        obj.save()
        return super(ProdutoCreate, self).form_valid(form)


class ProdutoUpdate(UpdateView):
    model = oper_models.Produto
    success_url = reverse_lazy('produto_list')
    fields = ['nome', 'descricao', 'qtd']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.updated_by = self.request.user
        obj.save()
        return super(ProdutoUpdate, self).form_valid(form)


class ProdutoDelete(DeleteView):
    model = oper_models.Produto
    success_url = reverse_lazy('produto_list')
