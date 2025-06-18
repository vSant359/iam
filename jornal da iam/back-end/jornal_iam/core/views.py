from django.shortcuts import render
from .models import Edicao, Destaques, Outros_grupos

def home(request):
    destaques = Destaques.objects.order_by('ordem')
    outros_grupos = Outros_grupos.objects.order_by('ordem')
    return render(request, 'core/home.html', {
    'destaques': destaques,
    'outros_grupos': outros_grupos
})
    

def edicoes(request):
    edicoes = Edicao.objects.all()
    return render(request, 'core/edicoes.html', {'edicoes': edicoes})

