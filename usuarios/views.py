from django.shortcuts import render
from .forms import FormDatosPersonales, FormDatosLaborales


def usuario(request):

	if request.method == 'POST':
		form_personales = FormDatosPersonales(request.POST, prefix='personales')
		form_laborales = FormDatosLaborales(request.POST, prefix='laborales')

		if form_personales.is_valid() and form_laborales.is_valid():
			print ("all validation passed")
			print (form_personales)
			print (form_laborales)
			form_personales.save()
			form_laborales.save()

		else:
			print ("failed")
	
	else:
		form_personales = FormDatosPersonales(prefix = 'personales')
		form_laborales = FormDatosLaborales(prefix = 'laborales')

	return render(
		request, 'usuario.html', 
		{'form_per': form_personales, 'form_lab': form_laborales}
	)
