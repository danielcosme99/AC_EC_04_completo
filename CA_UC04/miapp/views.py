from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from miapp import models

# Create your views here.
layout = """"""
def integrantes(request):
    integrantes = ['Alanya Villar Joel Edwin','Cosme Hernandez Carlos Daniel']
    return render(request, 'integrantes.html', {
        'titulo':'Integrantes del proyecto',
        'integrantes':integrantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo':'Bienvenidos',
        'mensaje':'Proyecto para la Unidad de Competencia 04 (UC04)'
    })

