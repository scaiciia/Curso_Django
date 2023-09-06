import sqlite3
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from . import forms
import sqlite3
from .models import Remera

# Create your views here.
def index(request):
    remeras = Remera.objects.all()
    ctx = {"remeras" : remeras}
    return render(request, "shop/index.html", ctx)

def contacto(request):
    return render(request, "shop/contacto.html")

def nueva_remera(request):
    if request.method == "POST":
        form = forms.FormularioRemeras(request.POST)
        if form.is_valid():
            Remera.objects.create(
                marca = form.cleaned_data["marca"],
                talle = form.cleaned_data["talle"],
                color = form.cleaned_data["color"],
                lisa = form.cleaned_data["lisa"],
                genero = form.cleaned_data["genero"]
            )
            return HttpResponseRedirect(reverse("index"))
    else:
        form = forms.FormularioRemeras()
    ctx = {"form" : form}
    return render(request, "shop/nueva_remera.html", ctx)