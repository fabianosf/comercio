from django.db import models

class Categoria(models.Model):
    CATEGORIA_CHOICES = (
        ('Brinquedo','Brinquedo'),
        ('Roupa', 'Roupa'),
        ('Sapato', 'Sapato'),
        ('Camisa', 'Camisa'),
        ('Esportes', 'Esporte'),
        ('Eletronico', 'Eletronico'),
    )
    nome = models.CharField('Categoria', max_length=12, choices=CATEGORIA_CHOICES)
    descricao = models.CharField('Descricao', max_length=50)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome
