from django.db import models

class DirectorPelicula(models.Model):
    nombre = models.CharField(max_length=32,help_text="Nombre Director")
    apellido = models.CharField(max_length=32,help_text="Apellidos Director")
    fechaNacimiento = models.DateField(help_text="Fecha nacimiento")

    def __str__(self):
        return self.nombre+" "+self.apellido


class Pelicula(models.Model):
    director = models.ForeignKey('DirectorPelicula', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=32,help_text="Nombre Pelicula")
    descripcion = models.TextField(max_length=100, help_text="Descripcion pelicula")
    duracion = models.PositiveIntegerField(help_text="Duracion en min")

    def __str__(self):
        return "Pelicula: "+self.nombre