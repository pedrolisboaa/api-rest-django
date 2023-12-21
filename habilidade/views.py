# Forma de ser realizada somente com DJANGO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Habilidade
from .serializers import HabilidadeSerializer

class HabilidadeLista(APIView):
    def get(self, request):
        habilidades = Habilidade.objects.all()
        serializer = HabilidadeSerializer(habilidades, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HabilidadeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class HabilidadeDetalhe(APIView):
    def get(self, request, pk):
        # try:
        #     habilidade = Habilidade.objects.get(pk=pk)
        # except Habilidade.DoesNotExist:
        #     return Response({'Erro': 'Habilidade não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        habilidade = get_object_or_404(Habilidade, pk=pk)
        serializer = HabilidadeSerializer(habilidade)
        return Response(serializer.data)
    
    def put(self, request, pk):
        habilidade = get_object_or_404(Habilidade, pk=pk)
        serializer = HabilidadeSerializer(habilidade, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        habilidade = get_object_or_404(Habilidade, pk=pk)
        habilidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        