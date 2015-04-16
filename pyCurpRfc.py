from general import *
from utils import *
class GenerarCURPRFC:

	def calculaCURP(self, nombre, ape_paterno, ape_materno, fecha_nacimiento, genero, entidad_federativa, origen):
		
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

		# Obtine datos generales del CURP
		curp = General.datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento, origen)
		clave_estado = General.entidadFederativa(entidad_federativa)
		# Agregamos el genero y lugar de nacimiento
		curp += genero + clave_estado
		# Obtener consonante Apellido Paterno
		curp = General.consonante(curp, ape_paterno)
		# Obtener consonante Apellido Materno
		curp = General.consonante(curp, ape_materno)
		# Obtener consonante Nombre
		curp = General.consonante(curp, nombre)
		# Obtiene Año de Nacimiento
		anio = Utils.anioFecha(fecha_nacimiento)
		# Agregar homoclave y digito verificador
		curp = General.digitoVerificador(curp, anio)
		print("CURP : "+curp)

	def calcularRFC(self, nombre, ape_paterno, ape_materno, fecha_nacimiento, genero):
		# Cambiamos todo a mayúsculas
		nombre = nombre.upper()
		ape_paterno = ape_paterno.upper()
		ape_materno = ape_materno.upper()
		# Quitamos los espacios al principio y final del nombre y apellidos
		nombre = nombre.strip()
		apellido_paterno = ape_paterno.strip()
		apellido_materno = ape_materno.strip()
		# Quitamos los artículos de los apellidos
		apellido_paterno = Utils.quitaArticulo(apellido_paterno)
		apellido_materno = Utils.quitaArticulo(apellido_materno)
		# Quitamos nombres Jose y Maria
		nombre = Utils.quitaNombre(nombre)
		# Quita la CH y la LL
		apellido_paterno = Utils.quitarCHLL(apellido_paterno)
		apellido_materno = Utils.quitarCHLL(apellido_materno)
		nombre = Utils.quitarCHLL(nombre)
	
		nombre_completo = ape_paterno +" "+ ape_materno +" "+ nombre
		origen = "RFC"

		rfc = General.datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento, origen)
		
		rfc = General.calculaHomoclaveRFC(rfc, nombre_completo)
		print("RFC  : "+rfc)
		
# Parametros
nombre = "giovani"
ape_paterno = "hidalgo"
ape_materno = "ostoa"
fecha_nacimiento = "12-08-1988"
genero = "H"
entidad_federativa = "HIDALGO"
origen = "CURP"

# Instancia de Clase
cp = GenerarCURPRFC()
cp.calculaCURP(nombre, ape_paterno, ape_materno, fecha_nacimiento, genero, entidad_federativa, origen)
cp.calcularRFC(nombre, ape_paterno, ape_materno, fecha_nacimiento, genero)  