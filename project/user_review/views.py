from django.shortcuts import render
from .forms import LibroForm, PeliculaForm, UsuarioForm


def index(request):
    return render(request, "user_review/index.html")


def review_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user_review/index.html')
    else:
        form = LibroForm()
    return render(request, 'user_review/review_libro.html', {'form': form})


def review_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user_review/index.html')
    else:
        form = PeliculaForm()
    return render(request, 'user_review/review_pelicula.html', {'form': form})


def insertar_usuario(request):
    # Lógica para insertar un usuario
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user_review/index.html')
    else:
        form = UsuarioForm()
    return render(request, 'insertar_usuario.html', {'form': form})
