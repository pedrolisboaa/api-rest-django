from django.contrib import admin
from .models import Vaga

# Register your models here.
@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'local', 'salario', 'ativa')
    list_filter = ('ativa', 'empresa')
    search_fields = ('titulo', 'descricao', 'empresa', 'local')
    ordering = ('-ativa', 'titulo')
    filter_horizontal = ('habilidades',)