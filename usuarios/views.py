from django.shortcuts import render
from .forms import FormDatosPersonales, FormDatosLaborales, FormOtro


def usuario(request):

	if request.method == 'POST':
		form_personales = FormDatosPersonales(request.POST, prefix='personales')
		form_laborales = FormDatosLaborales(request.POST, prefix='laborales')
		form_otro = FormOtro(request.POST, prefix = 'otro')


		if form_personales.is_valid() and form_laborales.is_valid():
			print ("all validation passed")
			print (form_personales)
			print (form_laborales)
			print (form_otro)
			form_personales.save()
			form_laborales.save()
			form_otro.save()

		else:
			print ("failed")
	
	else:
		form_personales = FormDatosPersonales(prefix = 'personales')
		form_laborales = FormDatosLaborales(prefix = 'laborales')
		form_otro = FormOtro(prefix = 'otro')

	return render(
		request, 'usuario.html', 
		{'form_per': form_personales, 'form_lab': form_laborales, 'form_otro':form_otro}
	)
