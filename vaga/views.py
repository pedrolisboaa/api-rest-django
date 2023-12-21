from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Vaga
from .serializers import VagaSerializer


class VagaLista(APIView):
    def get(self, request):
        vagas = Vaga.objects.filter(ativa=True)
        seriealizer = VagaSerializer(vagas, many=True)
        return Response(seriealizer.data)
    
    def post(self, request):
        serializer = VagaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class VagaDetalhe(APIView):
    def get(self, request, pk):
        vaga = get_object_or_404(Vaga, pk=pk, ativa=True)
        serializer = VagaSerializer(vaga)
        return Response(serializer.data)
    
    def put(self, request, pk):
        vaga = get_object_or_404(Vaga, pk=pk, ativa=True)
        serializer = VagaSerializer(vaga, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        vaga = get_object_or_404(Vaga, pk=pk)
        vaga.ativa = False
        return Response(status=status.HTTP_204_NO_CONTENT)

