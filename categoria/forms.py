from django import forms
from django.forms import ModelForm
from .models import Categoria


class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ('nome','descricao')