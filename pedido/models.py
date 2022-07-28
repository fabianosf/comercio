from django.db import models


class Pedido(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )

    data_pedido = models.DateTimeField()
    nome = models.CharField('Nome', max_length=255)
    rua = models.CharField('Rua', max_length=255)
    cidade = models.CharField('Cidade', max_length=255)
    estado = models.CharField('Estado', max_length=255)
    telefone = models.CharField('Telefone', max_length=15)
    email = models.EmailField()
    subtotal = models.DecimalField('Subtotal', decimal_places=2, max_digits=8)
    total = models.DecimalField('Total', decimal_places=2, max_digits=8)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.nome
    