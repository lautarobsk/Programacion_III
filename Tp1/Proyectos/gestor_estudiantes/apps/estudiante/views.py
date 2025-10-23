from django.shortcuts import render, get_object_or_404, redirect

from apps.estudiante.forms import EstudianteForm
from apps.estudiante.models import Estudiante, Curso
from django.contrib import messages
from django.urls import reverse


def index(request):
    return render(request, 'estudiante/index.html')

def alta_estudiante(request):
    return render(request, 'estudiante/alta_estudiante.html')

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'estudiante/lista_cursos.html', {'cursos': cursos})

def agregar_estudiante(request):
    mensaje = None
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "✅ Estudiante agregado correctamente."
            form = EstudianteForm()  # limpia el formulario
    else:
        form = EstudianteForm()

    return render(request, 'estudiante/agregar_estudiante.html', {'form': form, 'mensaje': mensaje})


def listar_estudiante(request):
    estudiantes = Estudiante.objects.select_related('curso').all()
    return render(request, 'estudiante/listar_estudiantes.html', {'estudiantes': estudiantes})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    estudiantes = curso.estudiante_set.all()  # obtiene todos los estudiantes de ese curso
    return render(request, 'estudiante/detalle_curso.html', {
        'curso': curso,
        'estudiantes': estudiantes
    })







