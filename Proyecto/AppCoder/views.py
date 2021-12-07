from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,context
# Create your views here.

def prueba(request):
    return HttpResponse('Prueba')

def Template(self):
    
    nombre = 'Pepe'
    apellido = 'Saltarin'
    
    mi_dict = {'key': 'value'}
    
    mis_datos = {'nombre': nombre, 'apellido': apellido, 'mi_dict': mi_dict, 'lista': [1,2,3,4,5,6]}
    
    plantilla = loader.get_template('C:/Tomas/Entrega/Proyecto/AppCoder/templates/AppCoder/Inicio.html')

    documento = plantilla.render(mis_datos)

    return HttpResponse(documento)