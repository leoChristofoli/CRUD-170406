# CRUD-170406

Sistema CRUD feito em Python sobre o framework django.

- [ ] Banco de dados preferencialmente NoSQL

- [x] As operações que manipulam dados devem ser autenticadas

- [x] Testes do código (livre escolha)

- [x] Deploy em um PaaS, ou em algum outro serviço na nuvem

- [x] O código deve ser publicado no Github

Foram usadas CBVs (Class based views) para agilizar o desenvolvimento:

isso:
```Python
class ServerCreate(CreateView):
    model = Server
    success_url = reverse_lazy('server_list')
    fields = ['name', 'ip', 'order']
```
invés disso:
