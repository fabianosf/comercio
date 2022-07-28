from tabnanny import verbose
from django.db import models

from produto.models import Produto

class Item(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='itens')
    quantidade = models.IntegerField('Quantidade')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.produto + self.quantidade
