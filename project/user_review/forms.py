from django import forms
from .models import Libro, Pelicula, User


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
