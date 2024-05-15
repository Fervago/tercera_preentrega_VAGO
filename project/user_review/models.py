from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100, default='Desconocido')
    autor = models.CharField(max_length=100, default='Autor Desconocido')
    reseña = models.TextField(null=True)


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100, default='Desconocido')
    director = models.CharField(max_length=100, default='Director Desconocido')
    reseña = models.TextField(null=True)


class User(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(null=True)
