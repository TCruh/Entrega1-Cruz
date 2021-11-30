from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def Template(self):
    
    #Info
    
    #Datos
    
    datos = {}
    
    #Plantilla
    
    plantilla = loader.get_template('inicio.html')
    
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)