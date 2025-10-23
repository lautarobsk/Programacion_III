from django.urls import path
from apps.estudiante import views

app_name = 'estudiante'

urlpatterns = [
    path('', views.index, name='index'),
    path('alta', views.alta_estudiante, name='alta_estudiante'),
    path('listar_cursos', views.listar_cursos, name='listar_cursos'),
    path('agregar', views.agregar_estudiante, name='agregar_estudiante'),
    path('listar_estudiantes', views.listar_estudiante, name='listar_estudiantes'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
]