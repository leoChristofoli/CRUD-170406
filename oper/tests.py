# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client

from oper.models import Produto
from datetime import datetime


class ProdutoTestCase(TestCase):

    def setUp(self):
        Produto.objects.create(nome="a0001", qtd=1)
        Produto.objects.create(nome="a0002", qtd=1000)

    def produto_when_created_is_now(self):
        prod = Produto.objects.get(nome='a0001')
        self.assertEqual(prod.when_created.date(), datetime.now().date())

    def test_prod_detail(self):
        nome = 'a0001'
        prod = Produto.objects.get(nome=nome)
        c = Client()
        url = '/produto/detail/{id}'.format(id=prod.id)
        response = c.get(url)
        self.assertEqual(response.context[-1]['object'].nome, nome)

    def test_prod_update(self):
        nome = 'a0001'
        c = Client()
        prod = Produto.objects.get(id=1)
        url = '/produto/detail/{id}'.format(id=prod.id)
        response = c.post(url, {
            'nome': 'a0003'
        })
        prod = Produto.objects.get(id=1)
        print(prod.nome)


class LoginTestCase(TestCase):

    def test_user_can_login(self):
        c = Client()
        response = c.get('/accounts/logout/')
        response = c.post('/accounts/login', {'email': 'leochp@gmail.com', 'password': '1'})
        self.assertEqual(response.status_code, 301)

    def test_redirect_to_list(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 302)

    def test_prod_list(self):
        c = Client()
        response = c.get('/produto/')
        self.assertEqual(response.content.strip().splitlines()[0], '<!DOCTYPE html>')

