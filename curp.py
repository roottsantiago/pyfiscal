
from utils import *
class curp:

	def calculaCurp(self):  
		test = 'prueba'

	def general(self):
		nom = "Tomas"
		apa = "Santiago"
		ama = "Gonzalez"
		fechaNacimiento = "16-11-1989"
		genero = "H"
		lugar_nacimiento = "HG"

		#RFC que se regresará
		curp = ""
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
			curp = utils.calculaOrigenCurp(nombre, apellidoPaterno, apellidoMaterno);
		# Verificar el curp que no tenga palabras obsenas 
		curp = utils.verificarPalabras(curp, origen)
		#Agregamos la fecha de Nacimiento
		curp = utils.fechaNacimiento(curp, fechaNacimiento)

		curp += genero + lugar_nacimiento
		print(curp)

		# Obtener consonante apellido paterno
		#consonante = "";
		#if apellidoPaterno != "":
		#	consonante = utils.getConsonate(apellidoPaterno)
		#	if consonante != "":
		#		consonante = "X";
		#		curp = curp + consonante
		#	else:
		#		curp = curp + "X"


cp = curp()
cp.calculaCurp()
cp.general()   