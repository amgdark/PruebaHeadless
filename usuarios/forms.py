from django import forms
from .models import DatosPersonales, DatosLaborales

class FormDatosPersonales(forms.ModelForm):
	
	class Meta:
		model = DatosPersonales
		fields = ('nombre', 'telefono', 'direccion', 'colonia')


class FormDatosLaborales(forms.ModelForm):
	
	class Meta:
		model = DatosLaborales
		fields = ('puesto', 'salario', )
