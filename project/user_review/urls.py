from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path("", views.index, name="index"),
    path("reviews/movie/", views.buscar_reviews_peliculas, name="lista_reviews_peliculas"),
     path("reviews/book/", views.buscar_reviews_libros, name="lista_reviews_libros"),
    path("user/", views.insertar_user, name="insertar_user"),
    path('add/book/', views.review_libro, name='review_libro'),
    path('add/movie/', views.review_pelicula, name='review_pelicula'),
]
