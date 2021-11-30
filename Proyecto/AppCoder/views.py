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
    
    # # # otra forma de render - otra forma de manejar archivo
    # miHtml = open("C:\Source Code\Clase17\Clase17\plantillas\prueba.html")

    # plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    # ##OJO importar template y contex, con: from django.template import Template, Context

    # miHtml.close() #Cerramos el archivo

    # miContexto = Context(mis_datos) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    # documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    
    plantilla = loader.get_template('AppCoder/Inicio.html')

    documento = plantilla.render(mis_datos)

    return HttpResponse(documento)