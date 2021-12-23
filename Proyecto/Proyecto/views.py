from django.http import HttpResponse
from django.template import loader

def prueba(request):
    return HttpResponse('Respuesta.')

def Template(self):
    
    #Info
    
    #Datos
    
    datos = {}
    
    #Plantilla
    
    plantilla = loader.get_template('index.html')
    
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)