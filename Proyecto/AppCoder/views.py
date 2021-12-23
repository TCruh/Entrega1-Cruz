from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader,context
# Create your views here.

def prueba(request):
    return HttpResponse('Prueba')

def Template(self):
    
    plantilla = loader.get_template('AppCoder/index.html')

    documento = plantilla.render({})

    return HttpResponse(documento)