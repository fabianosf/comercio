from django.urls import path
from .views import OfertaView

urlpatterns = [   
    path('oferta/', OfertaView.as_view(), name='oferta'), # rota index
]



