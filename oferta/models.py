from django.db import models
from produto.models import Produto

class Oferta(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='ofertas')
    descricao = models.CharField('Descricao Produto', max_length=150)

    class Meta: 
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        return self.descricao
