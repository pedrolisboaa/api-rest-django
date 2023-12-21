# Forma de ser realizada somente com DJANGO

from django.views import View
from django.http import JsonResponse
from .models import Habilidade

class HabilidadeLista(View):
    def get(self, request):
        habilidade = Habilidade.objects.all()
        return JsonResponse(habilidade, safe=False)
