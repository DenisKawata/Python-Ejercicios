from django.shortcuts import render

from django.shortcuts import render, HttpResponse
from .models import DirectorPelicula, Pelicula


def home(request):
    directores = DirectorPelicula.objects.all()
    return render(request, "directores/home.html",context={'directores':directores})

def pelicula(request):
    pelicula = Pelicula.objects.all()
    return render(request, "directores/pelicula.html",context={'pelicula':pelicula})