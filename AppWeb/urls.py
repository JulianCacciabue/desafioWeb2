from django.urls import path, include
from AppWeb.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("participantes/", participantes, name="Participantes"),
    path("competencias/", competencias, name="Competencias"),
    path("lugar/", lugar, name="Lugar"),
    #path("inscripcion/",inscripcion, name="Inscripcion" ),
    path("formulario/",inscripcion, name = "Formulario"),
    #path("AppWeb/", include(AppWeb.urls))
]
