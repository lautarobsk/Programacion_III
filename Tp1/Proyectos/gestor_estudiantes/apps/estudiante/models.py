from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_horas = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    nota_curso = models.DecimalField(max_digits=4, decimal_places=2)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
