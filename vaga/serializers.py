from rest_framework import serializers
from .models import Vaga

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        exclude = 'ativa',