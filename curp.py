from general import *
from utils import *
class generarCURPRFC:

	def calculaCURP(self, nombre, ape_paterno, ape_materno, fecha_nacimiento, genero, lugar_nacimiento, origen):
		# Obtine datos generales del CURP
		curp = general.datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento, origen)

		# Agregamos el genero y lugar de nacimiento
		curp += genero + lugar_nacimiento
		# Cambiamos todo a mayúsculas
		nombre = nombre.upper()
		ape_paterno = ape_paterno.upper()
		ape_materno = ape_materno.upper()
		# Quitamos los espacios al principio y final del nombre y apellidos
		nombre = nombre.strip()
		ape_paterno = ape_paterno.strip()
		ape_materno = ape_materno.strip()
		# Quitamos los artículos de los apellidos
		ape_paterno = utils.quitaArticulo(ape_paterno)
		ape_materno = utils.quitaArticulo(ape_materno)
		# Quitamos nombres Jose y Maria
		nombre = utils.quitaNombre(nombre)
		# Quita la CH y la LL
		ape_paterno = utils.quitarCHLL(ape_paterno)
		ape_materno = utils.quitarCHLL(ape_materno)
		nombre = utils.quitarCHLL(nombre)
		# Obtener consonante Apellido Paterno
		curp = general.getConsonante(curp, ape_paterno)
		# Obtener consonante Apellido Materno
		curp = general.getConsonante(curp, ape_materno)
		# Obtener consonante Nombre
		curp = general.getConsonante(curp, nombre)
		# Obtiene Año de Nacimiento
		anio = utils.getAnioFechaNac(fecha_nacimiento)
		# Agregar homoclave y digito verificador
		curp = utils.digitoVerificador(curp, anio)
		print("CURP : "+curp)

	def calcularRFC(self, nombre, ape_paterno, ape_materno, fecha_nacimiento, genero, lugar_nacimiento):
		nombre_completo = ape_paterno +" "+ ape_materno +" "+ nombre
		origen = "RFC"
		rfc = general.datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento, origen)
		
		rfc = general.calculaHomoclaveRFC(rfc, nombre_completo)
		print("RFC  : "+rfc)
		
# Parametros
nombre = "TOMAS"
ape_paterno = "SANTIAGO"
ape_materno = "GONZALEZ"
fecha_nacimiento = "16-11-1989"
genero = "H"
lugar_nacimiento = "HG"
origen = "CURP"

# Instancia de Clase
cp = generarCURPRFC()
cp.calculaCURP(nombre, ape_paterno, ape_materno, fecha_nacimiento, genero, lugar_nacimiento, origen)
cp.calcularRFC(nombre, ape_paterno, ape_materno, fecha_nacimiento, genero, lugar_nacimiento)  