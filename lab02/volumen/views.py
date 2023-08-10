import math
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "Volumen",
    }
    return render(request, 'volumen/ciclindro.html', context)

def enviar(request):
    resultado = float(request.POST['altura'])* float(request.POST['diametro'])/2**2 * float(request.POST['diametro']) * math.pi
    context = {
        'titulo'    : "Volumen",
        'altura'    : float(request.POST['altura']),
        'diametro'  : float(request.POST['diametro']),
        'pi'        : math.pi,
        'resultado' : resultado,       
    }
    return render(request, 'volumen/respuesta.html', context)
   