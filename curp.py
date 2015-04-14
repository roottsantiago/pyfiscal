from general import *
from utils import *
class generarCURPRFC:

	def calculaCurp(self):
		nombre = "Tomas"
		ape_paterno = "Santiago"
		ape_materno = "Gonzalez"
		fecha_nacimiento = "16-11-1989"
		genero = "H"
		lugar_nacimiento = "HG"
		origen = "CURP"
		curp = general.datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento, origen)

		#Agregamos el genero y lugar de nacimiento
		curp += genero + lugar_nacimiento

		#Cambiamos todo a mayúsculas
		nombre = nombre.upper()
		apellidoPaterno = ape_paterno.upper()
		apellidoMaterno = ape_materno.upper()

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


		# Obtener consonante Apellido Paterno
		consonante = "";
		if apellidoMaterno != "":
			consonante = utils.getConsonateCurp(apellidoMaterno)
			if consonante != "":
				curp = curp + consonante
			else:
				constante = "X";
				curp = curp + constante
		else:
			curp = curp + "X"

		# Obtener consonante Apellido Materno
		if apellidoMaterno != "":
			consonante = utils.getConsonateCurp(apellidoMaterno)
			if consonante != "":
				curp = curp + consonante
			else:
				constante = "X";
				curp = curp + constante
		else:
			curp = curp + "X"

		# Obtener consonante Nombre
		if nombre != "":
			consonante = utils.getConsonateCurp(nombre)
			if consonante != "":
				curp = curp + consonante
			else:
				constante = "X";
				curp = curp + constante
		else:
			curp = curp + "X"

		anio = utils.getAnioFechaNac(fecha_nacimiento)
		curp = utils.digitoVerificador(curp, anio)

		print(curp)

cp = generarCURPRFC()
cp.calculaCurp()  