from base import *
from utils import *


class Calcule(object):

	_nombres = None
	_apellido_paterno = None
	_apellido_materno = None
	_fecha_nacimiento = None
	_genero = None
	_lugar_nacimiento = None 

	def __init__(self):
		self._nombres = self.nombres
		self._apellido_paterno = self.apellido_paterno
		self._apellido_materno = self.apellido_materno
		self._fecha_nacimiento = self.fecha_nacimiento
		self._genero = self.genero
		self._lugar_nacimiento = self.lugar_nacimiento

	def CURP(self):	

		# Cambiamos todo a mayúsculas
		self._nombres = self._nombres.upper()
		self._apellido_paterno = self._apellido_paterno.upper()
		self._apellido_materno = self._apellido_materno.upper()
		self._lugar_nacimiento = self._lugar_nacimiento.upper()

		# Quitamos los espacios al principio y final del nombre y apellidos
		self._nombres = self._nombres.strip()
		self._apellido_paterno = self._apellido_paterno.strip()
		self._apellido_materno = self._apellido_materno.strip()

		# Quitamos los artículos de los apellidos
		self._apellido_paterno = Utils.quitaArticulo(self._apellido_paterno)
		self._apellido_materno = Utils.quitaArticulo(self._apellido_materno)

		# Quitamos nombres Jose y Maria
		self._nombres = Utils.quitaNombre(self._nombres)

		# Quita la CH y la LL
		self._apellido_paterno = Utils.quitarCHLL(self._apellido_paterno)
		self._apellido_materno = Utils.quitarCHLL(self._apellido_materno)
		self._nombres = Utils.quitarCHLL(self._nombres)

		# Obtine datos generales del CURP
		curp = General.datosGenerales(self._nombres, self._apellido_paterno, self._apellido_materno, self.fecha_nacimiento)
		clave_estado = General.entidad_federativa(self._lugar_nacimiento)

		# Agregamos el genero y lugar de nacimiento
		curp += self._genero + clave_estado

		# Obtener consonante Apellido Paterno
		curp = General.consonante(curp, self._apellido_paterno)

		# Obtener consonante Apellido Materno
		curp = General.consonante(curp, self._apellido_materno)

		# Obtener consonante Nombre
		curp = General.consonante(curp, self._nombres)

		# Obtiene Año de Nacimiento
		anio = Utils.anioFecha(self._fecha_nacimiento)

		# Agregar homoclave y digito verificador
		curp = General.digito_verificador(curp, anio)

		return curp

	def RFC(self):

		# Cambiamos todo a mayúsculas
		self._nombres = self._nombres.upper()
		self._apellido_paterno = self._apellido_paterno.upper()
		self._apellido_materno = self._apellido_materno.upper()

		# Quitamos los espacios al principio y final del nombre y apellidos
		self._nombres = self._nombres.strip()
		self._apellido_paterno = self._apellido_paterno.strip()
		self._apellido_materno = self._apellido_materno.strip()

		# Quitamos los artículos de los apellidos
		self._apellido_paterno = Utils.quitaArticulo(self._apellido_paterno)
		self._apellido_materno = Utils.quitaArticulo(self._apellido_materno)

		# Quitamos nombres Jose y Maria
		self._nombres = Utils.quitaNombre(self._nombres)

		# Quita la CH y la LL
		self._apellido_paterno = Utils.quitarCHLL(self._apellido_paterno)
		self._apellido_materno = Utils.quitarCHLL(self._apellido_materno)
		self._nombres = Utils.quitarCHLL(self._nombres)

		nombre_completo = self._apellido_paterno +" "+ self._apellido_materno +" "+ self._nombres

		rfc = General.datosGenerales(self._nombres, self._apellido_paterno, self._apellido_materno, self._fecha_nacimiento)

		rfc = General.calcula_homoclave(rfc, nombre_completo)

		return rfc
