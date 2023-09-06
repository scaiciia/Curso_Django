import sqlite3
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from . import forms
import sqlite3
from .models import Curso, Instructor

import requests

def index (request):
    ctx = {
        "nombre": "Juan",
        "cursos": 5,
        "curso_actual": {"nombre": "Python & Django", "turno": "Noche"},
        "cursos_anteriores": ["Java", "PHP", "JavaScript", "Python"]
    }
    return render(request, "myapp/index.html", ctx)

def condicionales(request):
    ctx = {
        "nombre": "Juan",
        "cursos": 0
    }
    return render(request, "myapp/condicionales.html", ctx)

def bucles(request):
    ctx = {
        "alumnos": ["Juan", "Sofía", "Matias"]
    }
    return render(request, "myapp/bucles.html", ctx)

def acerca_de (request):
    return HttpResponse("Curso de Python y Django!")

def cursos (request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM cursos")
    html = """
    <html>
    <title>Lista de cursos</title>
    <table style="border: 1px solid">
    <thead>
    <tr>
    <th>Curso</th>
    <th>Inscriptos</th>
    </tr>
    </thead>
    """
    for (nombre, inscriptos) in cursor.fetchall():
        html += """
        <tr>
        <td> {} </td>
        <td> {} </td>
        </tr>
        """.format(nombre, inscriptos)
    html += "</table></html>"
    conn.close()
    return HttpResponse(html)

def cursos_json(request):
    response = JsonResponse(list(Curso.objects.values()), safe = False)
    return response

def cursos_templates(request):
    cursos = Curso.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "myapp/cursos_templates.html", ctx)

def curso(request, nombre_curso):
    try:
        curso = Curso.objects.get(nombre=nombre_curso)
    except Curso.DoesNotExist:
        raise Http404
    ctx = {"cursos": curso}
    return render(request, "myapp/curso.html", ctx)

def cotizacion_dolar(request):
    r = requests.get("https://api.bluelytics.com.ar/v2/latest")
    cotizacion = r.json()
    oficial = cotizacion["oficial"]
    html = """
        <html>
            <title>Cotizacion del dolar</title>
            <p><strong>Compra: </strong>{}</p>
            <p><strong>Venta: </strong>{}</p>
    """.format(oficial["value_buy"], oficial["value_sell"])
    return HttpResponse(html)

def aeropuertos(request):
    f = open('aeropuertos.csv', encoding = 'utf8')
    html = """
        <html>
            <title>Lista Aeropuerto</title>
            <table>
                <tr>
                    <th>Aeropuerto</th>
                    <th>Ciudad</th>
                    <th>Pais</th>
                </tr>
        """
    for linea in f:
        datos = linea.split(",")
        nombre = datos[1].replace('"', '')
        ciudad = datos[2].replace('"', '')
        pais = datos[3].replace('"', '')
        html += """
            <tr>
                <th>{}</th>
                <th>{}</th>
                <th>{}</th>
            </tr>
        """.format(nombre, ciudad, pais)
    f.close()
    html += "</table></html>"
    return HttpResponse(html)

def aeropuertos_json(request):
    f = open('aeropuertos.csv', encoding = 'utf8')
    json = []
    for linea in f:
        datos = linea.split(',')
        aeropuerto = {
            "nombre": datos[1].replace('"', ''),
            "ciudad": datos[2].replace('"', ''),
            "pais": datos[3].replace('"', '')
        }
        json.append(aeropuerto)
    f.close()
    return JsonResponse(json, safe = False)

def aeropuerto_templates(request):
    f = open('aeropuertos.csv', encoding = 'utf8')
    json = {}
    aeropuerto = []
    for linea in f:
        datos = linea.split(',')
        vuelo = [
            datos[1].replace('"', ''),
            datos[2].replace('"', ''),
            datos[3].replace('"', '')
        ]
        aeropuerto.append(vuelo)
        print(aeropuerto)
        json = {"aeropuertos" : aeropuerto}
    f.close()
    return render(request, "myapp/aeropuertos_templates.html", json)

def static(request):
    return render(request, "myapp/static.html")

def ext(request):
    return render(request, "myapp/ext-de-plantillas.html")

def vista(request, nom_peli, num_com):
    dato = [num_com, nom_peli]
    cdx = {"pelicula" : dato}
    return render(request, "myapp/patron.html", cdx)

def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            Curso.objects.create(nombre=form.cleaned_data["nombre"], inscriptos=form.cleaned_data["inscriptos"])
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormularioCurso()
    ctx = {"form" : form}
    return render(request, "myapp/nuevo_curso.html", ctx)

def nuevo_cursoMF(request):
    if request.method == "POST":
        form = forms.FormularioCursoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormularioCursoModelForm()
    ctx = {"form" : form}
    return render(request, "myapp/nuevo_curso.html", ctx)

def nueva_pelicula(request):
    if request.method == "POST":
        form = forms.FormularioPelicula(request.POST)
        if form.is_valid():
            datos = [form.cleaned_data["nombre"], form.cleaned_data["fecha_estreno"], form.cleaned_data["edad"], form.cleaned_data["preventa"]]
            ctx = { "pelicula" : datos }
            return render(request, "myapp/pelicula_nueva.html", ctx)
    else:
        form = forms.FormularioPelicula()
    ctx = {"form" : form}
    return render(request, "myapp/nueva_pelicula.html", ctx)

def instructores(request):
    instructor = Instructor.objects.all()
    ctx = { "instructores" : instructor }
    return render(request, "myapp/instructores.html", ctx)