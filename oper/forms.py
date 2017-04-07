from django.forms import ModelForm
from django import forms
from django.utils.text import slugify

from oper.models import Produto


class SlugNomeField(forms.CharField):
    def to_python(self, value):
        return slugify(value)


class ProdutoForm(ModelForm):

    nome = SlugNomeField()

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'qtd']
