from django.urls import path
from .views import HabilidadeLista, HabilidadeDetalhe


app_name = 'habilidade'
urlpatterns = [
    path('', HabilidadeLista.as_view(), name='lista'),
    path('<int:pk>', HabilidadeDetalhe.as_view(), name='detalhe'),
]
