from django.shortcuts import render
from .models import Director, Pelicula

def index(request):
    
    Directores = Director.objects.all()
    Peliculas = Pelicula.objects.all()
    
    return render(
        request,
        'index.html',
        context={
            'Directores': Directores,
            'Peliculas': Peliculas,
        }
    )
