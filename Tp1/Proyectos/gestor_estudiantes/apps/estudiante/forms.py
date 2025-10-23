from django import forms
from apps.estudiante.models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'apellido', 'edad', 'nota_curso', 'curso')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'nota_curso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nota del curso'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }

