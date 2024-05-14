from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path("", views.index, name="index"),
    path('insertar_libro/', views.review_libro, name='review_libro'),
    path('insertar_pelicula/', views.review_pelicula, name='review_pelicula'),
    path('insertar_usuario/', views.insertar_usuario, name='insertar_usuario'),
]