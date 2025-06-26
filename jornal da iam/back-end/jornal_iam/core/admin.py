from django.contrib import admin
from .models import Edicao, Destaques, Outros_grupos

@admin.register(Edicao)
class EdicaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'publicado_em']
    search_fields = ['titulo']
    list_filter = ['publicado_em']

@admin.register(Destaques)
class Destaques(admin.ModelAdmin):
    list_display =['id', 'imagem',  'ordem']
    ordering = ['ordem']

@admin.register(Outros_grupos)
class Outros_grupos(admin.ModelAdmin):
    list_display = ['id', 'imagem', 'descricao', 'ordem']
    ordering = ['ordem']