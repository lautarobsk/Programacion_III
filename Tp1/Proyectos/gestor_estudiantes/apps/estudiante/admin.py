from django.contrib import admin

from apps.estudiante.models import Estudiante, Curso

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'nota_curso', 'curso')
    #search_fields = ('nombre', 'apellido', 'edad', 'nota_curso', 'curso')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
    #search_fields = ('nombre', )

