from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    biografia = models.TextField()
    foto = models.URLField(max_length=540, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellidos

class Pelicula(models.Model):
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25)
    trama = models.TextField()
    caratula = models.URLField(max_length=540, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.nombre
