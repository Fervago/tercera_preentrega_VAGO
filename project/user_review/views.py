from django.shortcuts import render
from . import models
from .forms import LibroForm, PeliculaForm, UsuarioForm


def index(request):
    return render(request, "user_review/index.html")


def review_libro(request):
    "Gaurada la resena en la BD"
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user_review/index.html')
    else:
        form = LibroForm()
    return render(request, 'user_review/review_libro.html', {'form': form})


def review_pelicula(request):
    "Gaurada la resena en la BD"
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user_review/index.html')
    else:
        form = PeliculaForm()
    return render(request, 'user_review/review_pelicula.html', {'form': form})


def insertar_user(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user_review/index.html')
    else:
        form = UsuarioForm()
    return render(request, 'user_review/insertar_user.html', {'form': form})


def buscar_reviews_libros(request):
    "Obtener las reseñas de libros de la base de datos"
    book_reviews = models.Libro.objects.all()
    return render(request, 'user_review/lista_reviews_libros.html', {'book_reviews': book_reviews})


def buscar_reviews_peliculas(request):
    "Obtener las reseñas de peliculas de la base de datos"
    movie_reviews = models.Pelicula.objects.all()
    return render(request, 'user_review/lista_reviews_peliculas.html', {'movie_reviews': movie_reviews})
