
from django.db import models

class DatosPersonales(models.Model):
	nombre = models.CharField('Nombre',max_length=200)
	telefono = models.CharField(u'Telefono',max_length=13)
	direccion = models.CharField(u'Direccion',max_length=100)
	colonia = models.CharField(u"Colonia", max_length=50)
	
	def __str__(self):
		return self.nombre
		
class DatosLaborales(models.Model):
	puesto = models.CharField('Puesto',max_length=100)
	salario = models.DecimalField(u'Salario',decimal_places=2, max_digits=4)
	
	def __str__(self):
		return self.puesto

class DatosOtros(models.Model):
	otro = models.CharField('Otro',max_length=100)
	
	def __str__(self):
		return self.otro