from django.urls import path
from .views import  VagaLista, VagaDetalhe


app_name = 'vaga'
urlpatterns = [
    path('', VagaLista.as_view(), name='lista'),
    path('<int:pk>', VagaDetalhe.as_view(), name='detalhe'),
]
    

