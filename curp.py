
from utils import *
class curp:

	def calculaCurp(self):  
		test = 'prueba'

	def general(self):
		nom = "Tomas"
		apa = "Santiago"
		ama = "Gonzalez"
		fechaNacimiento = "16-11-1989"

		#RFC que se regresará
		rfc = ""
		#Cambiamos todo a mayúsculas
		nombre = nom.upper()
		apellidoPaterno = apa.upper()
		apellidoMaterno = ama.upper()
		#Quitamos los espacios al principio y final del nombre y apellidos
		nombre = nombre.strip()
		apellidoPaterno = apellidoPaterno.strip()
		apellidoMaterno = apellidoMaterno.strip()
		#Quitamos los artículos de los apellidos
		apellidoPaterno = utils.quitaArticulo(apellidoPaterno)
		apellidoMaterno = utils.quitaArticulo(apellidoMaterno)
		# Quitamos nombres Jose y Maria
		nombre = utils.quitaNombre(nombre)
		# Quita la CH y la LL
		apellidoPaterno = utils.quitarCHLL(apellidoPaterno)
		apellidoMaterno = utils.quitarCHLL(apellidoMaterno)
		nombre = utils.quitarCHLL(nombre)
		


		origen = 'CURP'
		if origen == "CURP":
			rfc = utils.calculaOrigenCurp(nombre, apellidoPaterno, apellidoMaterno);
		# Verificar el curp que no tenga palabras obsenas 
		rfc = utils.verificarPalabras(rfc, origen)
		#Agregamos la fecha de Nacimiento
		rfc = utils.fechaNacimiento(rfc, fechaNacimiento)
		print(rfc)

		# Obtener consonante apellido paterno
		#consonante = "";
		#if apellidoPaterno != "":
		#	consonante = utils.getConsonate(apellidoPaterno)
		#	if consonante != "":
		#		consonante = "X";
		#		rfc = rfc + consonante
		#	else:
		#		rfc = rfc + "X"


cp = curp()
cp.calculaCurp()
cp.general()   