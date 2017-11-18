Feature: Ingresar como administrador
	Como administrador de la aplicación
	Deseo ingresar al sistema
	Para realizar las actividades de gestión


	Scenario: Credenciales correctas
		Dado que ingreso la url "http://localhost:8000/admin"
		Y en las cajas de texto el usuario "alex" y la contraseña "alexcontra"
		Cuando presiono el botón ingresar
		Entonces puedo ver el mensaje "BIENVENIDO, ALEX"

	Scenario: Credenciales incorrectas
		Dado que ingreso la url "http://localhost:8000/admin"
		Y en las cajas de texto el usuario "alex" y la contraseña "alexcontrass"
		Cuando presiono el botón ingresar
		Entonces puedo ver el mensaje de error "Por favor introduza nombre de usuario y contraseña correctos"