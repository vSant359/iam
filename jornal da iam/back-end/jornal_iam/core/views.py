from django.shortcuts import render
from .models import Edicao

def home(request):
    return render(request, 'core/home.html')

def edicoes(request):
    edicoes = Edicao.objects.all()
    return render(request, 'core/edicoes.html', {'edicoes': edicoes})

