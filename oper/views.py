# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.text import slugify

from oper import models as oper_models
from oper.forms import ProdutoForm


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ProdutoList(ListView):
    model = oper_models.Produto


class DeletedProdutoList(ListView):
    model = oper_models.DeletedProduto
    template_name = 'oper/produto_list.html'


class ProdutoCreate(CreateView):
    model = oper_models.Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('produto_list')
    # fields = ['nome', 'descricao', 'qtd']

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

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        deleted = oper_models.DeletedProduto()
        deleted.nome = obj.nome
        deleted.descricao = obj.descricao
        deleted.qtd = obj.qtd
        deleted.when_created = obj.when_created
        deleted.when_updated = obj.when_updated
        deleted.client_ip = obj.client_ip
        deleted.created_by = obj.created_by
        deleted.updated_by = obj.updated_by
        deleted.save()
        return super(ProdutoDelete, self).delete(request)
