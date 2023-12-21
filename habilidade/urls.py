from django.urls import path
from .views import HabilidadeLista


app_name = 'habilidade',
urlpatterns = [
    path('', HabilidadeLista.as_view(), name='lista')
]
