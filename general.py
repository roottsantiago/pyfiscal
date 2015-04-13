from utils import *
class general:

	def generarRFC():
		nom = "Tomas"
		apa = "Santiago"
		ama = "Gonzalez"
		fechaNacimiento = "16-11-1989"
		genero = "H"
		lugar_nacimiento = "HG"

		#CURP que se regresará
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

		#Agregamos el genero y lugar de nacimiento
		curp += genero + lugar_nacimiento

		# Obtener consonante Apellido Paterno
		consonante = "";
		if apellidoPaterno != "":
			consonante = utils.getConsonateCurp(apellidoPaterno)
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

		anio = utils.getAnioFechaNac(fechaNacimiento)
		curp = utils.digitoVerificador(curp, anio)

		return curp