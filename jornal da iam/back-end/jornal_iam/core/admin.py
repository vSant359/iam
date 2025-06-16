from django.contrib import admin
from .models import Edicao

@admin.register(Edicao)
class EdicaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'publicado_em']
    search_fields = ['titulo']
    list_filter = ['publicado_em']
