from django import forms
from .models import DatosPersonales, DatosLaborales, DatosOtros

class FormDatosPersonales(forms.ModelForm):
	
	class Meta:
		model = DatosPersonales
		fields = ('nombre', 'telefono', 'direccion', 'colonia')


class FormDatosLaborales(forms.ModelForm):
	
	class Meta:
		model = DatosLaborales
		fields = ('puesto', 'salario', )


class FormOtro(forms.ModelForm):

	class Meta:
		model = DatosOtros
		fields = ('otro', )
