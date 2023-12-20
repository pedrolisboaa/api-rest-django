from django.db import models

# Create your models here.
class Vaga(models.Model):
    titulo = models.CharField(max_length=256)
    descricao = models.TextField()
    empresa = models.CharField(max_length=256)
    local = models.CharField(max_length=256)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null= True)
    ativa = models.BooleanField(default=True)
    habilidades = models.ManyToManyField('habilidade.Habilidade')
    
    def __str__(self):
        return self.titulo