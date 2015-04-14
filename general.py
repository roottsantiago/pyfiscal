from utils import *
from stringBuilder import*

class general:

	def datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento, origen):
		generico = ""

		# Cambiamos todo a mayúsculas
		nombre = nombre.upper()
		apellidoPaterno = ape_paterno.upper()
		apellidoMaterno = ape_materno.upper()

		# Quitamos los espacios al principio y final del nombre y apellidos
		nombre = nombre.strip()
		apellidoPaterno = apellidoPaterno.strip()
		apellidoMaterno = apellidoMaterno.strip()

		# Quitamos los artículos de los apellidos
		apellidoPaterno = utils.quitaArticulo(apellidoPaterno)
		apellidoMaterno = utils.quitaArticulo(apellidoMaterno)

		# Quitamos nombres Jose y Maria
		nombre = utils.quitaNombre(nombre)

		# Quita la CH y la LL
		apellidoPaterno = utils.quitarCHLL(apellidoPaterno)
		apellidoMaterno = utils.quitarCHLL(apellidoMaterno)
		nombre = utils.quitarCHLL(nombre)
		
		origen_curp = 'CURP'
		if origen_curp == origen:
			generico = utils.calculaOrigenCurp(nombre, apellidoPaterno, apellidoMaterno);

		# Verificar los datos que no tenga palabras obsenas 
		generico = utils.verificarPalabras(generico, origen)

		# Agregamos la fecha de Nacimiento
		generico = utils.fechaNacimiento(generico, fecha_nacimiento)
		return generico

	def calculaHomoclaveRFC(rfc, nombre_completo, fecha_nac):

		sb = StringBuilder()
		sb.Append("Hello\n")
		sb.Append("World")
		print(sb)