# CRUD-170406
https://fathomless-taiga-71479.herokuapp.com/


Sistema CRUD feito em Python sobre o framework django.

- [ ] Banco de dados preferencialmente NoSQL -

- [x] As operações que manipulam dados devem ser autenticadas - `Para esse teste, qualquer usuário **cadastrado** pode realizar as operações`

- [x] Testes do código (livre escolha) - `Usado o mecanismo padrão do Django e Selenium`
    
- [x] Deploy em um PaaS, ou em algum outro serviço na nuvem - `Heroku`

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

- [x] Ausência de controle de requisições - `Implementado um profiler básico, usando django-profiler`
- [x] O cookie de sessão trafega em meio sem criptografia. `SESSION_COOKIE_SECURE, que faz parte do middleware default security.SecurityMiddleware, foi ativado`
- [x] Ausência do cabeçalho HSTS. `SECURE_HSTS_SECONDS ativo`
- [x] Ausência de verificação de integridade SRI para componentes carregados externamente. `adicionado atributo integrity no jquery`
- [x] Ausência de uma política de segurança para conteúdo (cabeçalho CSP). `Utilizado o package disponibilizado pela mozilla, django-csp,
para configurar a política: `
- [ ] Log gravado client-side.
- [x] CVE-2017-7233 e CVE-2017-7234. `upgrade para django 1.10.7`
- [ ] Credenciais no código.
- [x] CVE-2016-9014.
- [ ] Recuperação de senha não funciona.
- [x] Falha na lógica de negócio. Número negativo de produtos no cadastro. `Alterado de IntegerField para PositiveIntegerField`