from django.shortcuts import render
from django.http import HttpResponse
from AppLuna.models import *
from AppLuna.forms import *

# Create your views here.

def inicio(request):

    return render(request,"AppLuna/inicio.html")


def perro(request):

    
    if request.method == "POST":

        formulario = PerroFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            perro = Perro(nombre=info["nombre"], raza=info["raza"], edad=info["edad"], sexo=info["sexo"])


            perro.save()

            return render(request,"AppLuna/inicio.html")

    else:
 
        formulario = PerroFormulario()

    return render(request,"AppLuna/perro.html", {"perro1":formulario})

   


def gato(request):

    if request.method == "POST":

        formulario = GatoFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            gato = Gato(nombre=info["nombre"], raza=info["raza"], edad=info["edad"], sexo=info["sexo"])


            gato.save()

            return render(request,"AppLuna/inicio.html")

    else:
 
        formulario = GatoFormulario()

    return render(request,"AppLuna/gato.html", {"gato1":formulario})






def roedor(request):

    if request.method == "POST":

        formulario = RoedorFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            roedor = Roedor(nombre=info["nombre"], raza=info["raza"], edad=info["edad"], sexo=info["sexo"])


            roedor.save()

            return render(request,"AppLuna/inicio.html")

    else:
 
        formulario = RoedorFormulario()

    return render(request,"AppLuna/roedor.html", {"roedor1":formulario})




def dueno(request):

    if request.method == "POST":

        formulario = DuenoFormulario(request.POST)

        if formulario.is_valid():

            info = formulario.cleaned_data

            dueno = Dueno(nombre=info["nombre"], edad=info["edad"])


            dueno.save()

            return render(request,"AppLuna/inicio.html")

    else:
 
        formulario = DuenoFormulario()

    return render(request,"AppLuna/dueno.html", {"dueno1":formulario})

    


def mascota(request):

    return render(request, "AppLuna/inicio.html")


def result(request):

    if request.GET["mascota"]:

        mascota = request.GET["mascota"]

        if Perro.objects.filter(nombre=mascota).exists():

            mascota=Perro.objects.get(nombre=mascota) #Si son mas de uno , no va a andar

        if Gato.objects.filter(nombre=mascota).exists():

            mascota=Gato.objects.get(nombre=mascota)

        if Roedor.objects.filter(nombre=mascota).exists():

            mascota=Roedor.objects.get(nombre=mascota)

       # dueno = Perro.objects.filter(nombre__iexact=mascota)
        
        return render(request, "AppLuna/inicio.html", {"mascota":mascota})

    else:

        respuesta = "No cargo informacíon."



    return HttpResponse(f"Tu Mascota es:{request.GET['mascota']}")