from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    monotributista = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Profesores"

class Curso(models.Model):
    nombre = models.CharField("Nombre", max_length=128)
    inscriptos = models.IntegerField("Inscriptos")
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche")
    )
    turno = models.PositiveSmallIntegerField("Turno", choices=TURNOS, null=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name="cursos")
    
    def __str__(self):
        return self.nombre
    
class Instructor(models.Model):
    nombre = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    cursos_asignados = models.IntegerField()