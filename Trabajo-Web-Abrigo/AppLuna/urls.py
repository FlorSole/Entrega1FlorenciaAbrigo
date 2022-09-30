
from django.urls import path
from AppLuna.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("dueno/", dueno, name="Dueño"),
    path("perros/", perro, name="Perros"),
    path("gatos/", gato, name="Gatos"),
    path("roedores/", roedor, name="Roedores"),
    path("mascota/", mascota, name="buscarmascota"),
    path("result/", result, name="TuMascota"),
]