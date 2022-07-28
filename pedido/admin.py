from django.contrib import admin
from .models import  Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('data_pedido','nome','cidade','telefone','email', 'total')



