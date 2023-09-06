from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("condicionales", views.condicionales, name = "condicionales"),
    path("bucles", views.bucles, name = "bucles"),
    path("acerca-de", views.acerca_de, name = "acerca_de"),
    path("cursos" , views.cursos, name = "cursos"),
    path("cursos/json" , views.cursos_json, name = "cursos_json"),
    path("cursos_templates", views.cursos_templates, name = "cursos_templates"),
    path("cotizacion-dolar", views.cotizacion_dolar, name = "cotizacion_dolar"),
    path("aeropuertos", views.aeropuertos, name = "aeropuertos"),
    path("aeropuertos/json", views.aeropuertos_json, name = "aeropuertos_json"),
    path("static", views.static, name = "static"),
    path("ext-de-plantillas", views.ext, name= "ext_de_plantillas"),
    path("curso/<str:nombre_curso>", views.curso, name="curso"),
    path("aeropuerto-templates", views.aeropuerto_templates, name="aeropuerto_templates"),
    path("peliculas/<str:nom_peli>/comentarios/<int:num_com>", views.vista, name="peliculas"),
    path("nuevo-curso", views.nuevo_curso, name="nuevo_curso"),
    path("nuevo-cursoMF", views.nuevo_cursoMF, name="nuevo_cursoMF"),
    path("nueva-pelicula", views.nueva_pelicula, name="nueva_pelicula"),
    path("instructores", views.instructores, name="instructores"),
]
