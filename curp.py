from general import *
from utils import *
class GenerarCURPRFC:

	def calculaCURP(self, nombre, ape_paterno, ape_materno, fecha_nacimiento, genero, lugar_nacimiento, origen):
		# Obtine datos generales del CURP
		curp = General.datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento, origen)

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
		ape_paterno = Utils.quitaArticulo(ape_paterno)
		ape_materno = Utils.quitaArticulo(ape_materno)
		# Quitamos nombres Jose y Maria
		nombre = Utils.quitaNombre(nombre)
		# Quita la CH y la LL
		ape_paterno = Utils.quitarCHLL(ape_paterno)
		ape_materno = Utils.quitarCHLL(ape_materno)
		nombre = Utils.quitarCHLL(nombre)
		# Obtener consonante Apellido Paterno
		curp = General.getConsonante(curp, ape_paterno)
		# Obtener consonante Apellido Materno
		curp = General.getConsonante(curp, ape_materno)
		# Obtener consonante Nombre
		curp = General.getConsonante(curp, nombre)
		# Obtiene Año de Nacimiento
		anio = Utils.getAnioFechaNac(fecha_nacimiento)
		# Agregar homoclave y digito verificador
		curp = General.digitoVerificador(curp, anio)
		print("CURP : "+curp)

	def calcularRFC(self, nombre, ape_paterno, ape_materno, fecha_nacimiento, genero, lugar_nacimiento):
		nombre_completo = ape_paterno +" "+ ape_materno +" "+ nombre
		origen = "RFC"
		rfc = General.datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento, origen)
		
		rfc = General.calculaHomoclaveRFC(rfc, nombre_completo)
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
cp = GenerarCURPRFC()
cp.calculaCURP(nombre, ape_paterno, ape_materno, fecha_nacimiento, genero, lugar_nacimiento, origen)
cp.calcularRFC(nombre, ape_paterno, ape_materno, fecha_nacimiento, genero, lugar_nacimiento)  