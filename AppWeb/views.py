from http.client import HTTPResponse
from django.shortcuts import render
from AppWeb.models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render(request, "AppWeb/inicio.html")

def participantes(request):

    part1 = Participante(nombre="Julian", edad = 30, correo="juliancacciabue@hotmail.com")
    part1.save()

    #return HttpResponse (f"El participante es {part1.nombre} y su edad es {part1.edad}")
    return render(request, "AppWeb/participantes.html")

def competencias(request):

    compe1 = Competencia(nombreCompetencia="Natacion")
    compe1.save()

    #return HttpResponse (f"La competencia es: {compe1.nombreCompetidor}")
    return render(request, "AppWeb/competencias.html")
def lugar(request):

    lugar1 = Lugar(nombreLugar="San Isidro")
    lugar1.save()

    #return HttpResponse (f"El lugar de la comeptencia es {lugar1.nombreLugar}")
    return render(request, "AppWeb/lugar.html")


def inscripcion(request):

    if request.method=="POST":

        participantesF = Participante(nombre=request.POST["nombre"], edad=request.POST["edad"], correo=request.POST["correo"])

        participantesF.save()

        return render(request, "AppWeb/inscribirse.html")
    
    
    return render(request, "AppWeb/inscribirse.html")
