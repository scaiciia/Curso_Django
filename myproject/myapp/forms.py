from django import forms
from django.forms import ModelForm
from .models import Curso

class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    inscriptos = forms.IntegerField(label="Inscriptos")
    solo_empresas = forms.BooleanField(label="Solo empresas?", required= False)
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche")
    )
    turnos = forms.ChoiceField(label="Turno", choices=TURNOS)
    fecha_inicio = forms.DateField(
        label="Fecha de inicio",
        input_formats=["%d/%m/%Y"],
    )
    fecha_fin = forms.DateField(
        label="Fecha de finalización",
        widget=forms.DateInput(attrs={"type" : "date"}),
    )

class FormularioPelicula(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=128)
    fecha_estreno = forms.DateField(
        label="Fecha de estreno:",
        widget=forms.DateInput(attrs={"type" : "date"})
    )
    edad = forms.IntegerField(label="Para mayores de:")
    preventa = forms.BooleanField(label="Preventa online?", required=False)
    
class FormularioCursoModelForm(ModelForm):
    class Meta:
        model = Curso
        fields = ("nombre", "inscriptos", "turno")
