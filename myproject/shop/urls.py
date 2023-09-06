from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("contacto", views.contacto, name = "contacto"),
    path("nueva-remera", views.nueva_remera, name= "nueva_remera")
]