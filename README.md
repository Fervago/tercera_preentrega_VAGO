# Nombre del Proyecto

<<<<<<< HEAD
=======
    ReviewSphere

>>>>>>> prueba
## Explicación breve del proyecto en cuanto al servicio

    Pagina web en la cual se pueden leer y publicar resenas.

## Explicación breve técnica: urls, modelos, plantillas

Estructura del Proyecto

Este proyecto está diseñado para proporcionar una plataforma interactiva de reseñas de libros y películas. A continuación, se detalla la estructura y funcionalidades clave del sistema.

Modelos

Los modelos son representaciones de la base de datos y definen la estructura de los datos que se manejarán dentro de la aplicación:

    Libro: Almacena información sobre libros, incluyendo el título, autor y una reseña textual.
    Pelicula: Guarda detalles de películas, como el título, director y reseña.
    User: Mantiene registros de los usuarios, con campos para el nombre y correo electrónico.

URLs

Las URLs son las rutas de acceso que conectan las solicitudes de los usuarios con las vistas correspondientes:

    Ruta principal ("/"): Dirige a la página de inicio de la aplicación.
    Reseñas de películas ("reviews/movie/"): Lista todas las reseñas de películas disponibles.
    Reseñas de libros ("reviews/book/"): Muestra las reseñas de libros.
    Nuevo usuario ("user/"): Permite la inserción de un nuevo usuario en el sistema.
    Añadir reseña de libro ('add/book/'): Ruta para publicar una nueva reseña de libro.
    Añadir reseña de película ('add/movie/'): Ruta para publicar una nueva reseña de película.

Plantillas

Las plantillas son archivos HTML que facilitan la presentación de datos en la interfaz de usuario. Utilizan la sintaxis del Lenguaje de Plantillas de Django para integrar datos dinámicos en la página web.

## Mejoras futuras

    Mejorar el ux y agregar mas funcionalidades, ademas de proporcionar una mejor seguridad a la pagina.

## Problemas conocidos

    El ux no es el optimo.
