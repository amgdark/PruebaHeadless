Feature: Ingresar como administrador
	Como administrador de la aplicación
	Deseo ingresar al sistema
	Para realizar las actividades de gestión


	Scenario: Credenciales correctas
		Dado que ingreso la url "http://localhost:8000/admin"
		Y en las cajas de texto el usuario "alex" y la contraseña "alexcontra"
		Cuando presiono el botón ingresar
		Entonces puedo ver el mensaje "WELCOME, ALEX"