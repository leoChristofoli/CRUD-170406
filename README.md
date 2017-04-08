# CRUD-170406
https://fathomless-taiga-71479.herokuapp.com/


Sistema CRUD feito em Python sobre o framework django.

- [ ] Banco de dados preferencialmente NoSQL -

- [x] As operações que manipulam dados devem ser autenticadas - Para esse teste, qualquer usuário **cadastrado** pode realizar as operações

- [x] Testes do código (livre escolha) - Usado o mecanismo padrão do Django
    
- [x] Deploy em um PaaS, ou em algum outro serviço na nuvem - Heroku

- [x] O código deve ser publicado no Github

Foram usadas CBVs (Class based views) para agilizar o desenvolvimento:

isso:
```Python
class ProdutoCreate(CreateView):
    model = oper_models.Produto
    success_url = reverse_lazy('produto_add')
    fields = ['nome', 'descricao', 'qtd']
```
em vez disso:
```Python
def produto_create(request, template_name='oper/produto_form.html'):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, template_name, {'form':form})
```

Para rodar os testes: `python manage.py test`
