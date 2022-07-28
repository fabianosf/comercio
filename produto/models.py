from django.db import models
from categoria.models import Categoria


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField('Nome do Produto', max_length=150)
    descricao = models.TextField('Descrição do Produto')
    preco = models.DecimalField('Preço do Produto', decimal_places=2, max_digits=8)
    imagem = models.ImageField(upload_to='media/img/', height_field=None, width_field=None, max_length=100, null='true')
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    
    def __str__(self):
        return self.nome

