from django.urls import path
from .views import PedidoView

urlpatterns = [   
    path('pedido/', PedidoView.as_view(), name='pedido'), # rota index
]