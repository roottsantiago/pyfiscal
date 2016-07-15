# -*- coding: utf-8 -*-

import datetime
from utils import Utils

class BaseGenerator(object):

	def genera(self):
		raise NotImplementedError("No implemetado.")

	def parse(self, nombres, paterno, materno=None, estado=None):

		if estado != None:
			self.estado = Utils().upper(estado)

		if materno is not None:
			self.materno = Utils().upper(materno)
			self.materno = Utils().quita_articulo(self.materno)
			self.materno = Utils().quita_CH_LL(self.materno)

		self.nombres = Utils().upper(nombres)
		self.paterno = Utils().upper(paterno)
	
		self.nombres = Utils().quita_nombre(self.nombres)
		self.paterno = Utils().quita_articulo(self.paterno)

		self.nombres = Utils().quita_CH_LL(self.nombres)
		self.paterno = Utils().quita_CH_LL(self.paterno)
		

	def base_dato_fiscal(self, nombres, paterno, materno, fecha):
		# Regresa iniciales del nombre y verifica palabras 
		dato_fiscal = self.iniciales_nombre(nombres, paterno, materno)
		dato_fiscal = self.verifica_palabra(dato_fiscal)
		# Agrega fecha de nacimineto
		fecha_nacimiento = self.parse_fecha(fecha)
		dato_fiscal += fecha_nacimiento

		return dato_fiscal
		
	def iniciales_nombre(self, nombres, paterno, materno):
		iniciales = ''
		# Inicial del apellido paterno
		iniciales = paterno[0:1]
		# Busca la primera vocal del apellido paterno
		vocal = Utils().busca_vocal(paterno)
		# Agrega vocal
		iniciales += vocal 
		# inicial del apellido materno y nombre
		if materno is None:
			iniciales += 'X'
		else:
			iniciales += materno[0:1]
		iniciales += nombres[0:1]

		return iniciales

	def verifica_palabra(self, rfc):

		palabras = [ 
			'BUEI', 'BUEY', 'CACA', 'CACO', 'CAGA', 'CAGO', 'CAKA', 'CAKO', 'COGE',
			'COGI', 'COJA', 'COJE', 'COJI', 'COJO', 'COLA', 'CULO', 'FALO', 'FETO',
			'GETA', 'GUEI', 'GUEY', 'JETA', 'JOTO', 'KACA', 'KACO', 'KAGA', 'KAGO', 
			'KAKA', 'KAKO', 'KOGE', 'KOGI', 'KOJA', 'KOJE', 'KOJI', 'KOJO', 'KOLA', 
			'KULO', 'LILO', 'LOCA', 'LOCO', 'LOKA', 'LOKO', 'MAME', 'MAMO', 'MEAR', 
			'MEAS', 'MEON', 'MIAR', 'MION', 'MOCO', 'MOKO', 'MULA', 'MULO', 'NACA', 
			'NACO', 'PEDA', 'PEDO', 'PENE', 'PIPI', 'PITO', 'POPO', 'PUTA', 'PUTO', 
			'QULO', 'RATA', 'ROBA', 'ROBE', 'ROBO', 'RUIN', 'SENO', 'TETA', 'VUEI', 
			'VUEY', 'WUEI', 'WUEY',
		]

		for palabra in palabras:
			if palabra == rfc:
				rfc = "XXXX"
				break

		return rfc

	def parse_fecha(self, fecha):
		fecha_nac = ""
		fecha_type = type(fecha)

		if fecha is None:
			fecha = datetime.datetime.today()
		else:
			if not (fecha_type is datetime.datetime or fecha_type is datetime.date):
				fecha = datetime.datetime.strptime(fecha, '%d-%m-%Y').date()
		
		
		anio = str(fecha.year)
		anio = anio[2:4]
		# Rellena con ceros a la izquierda
		mes = str(fecha.month).zfill(2)
		dia = str(fecha.day).zfill(2)
		fecha_nac += anio+mes+dia 

		return fecha_nac


	def entidad_federativa(self, param):
		estado = None	
		estados = { 
			'':'', 'AGUASCALIENTES':'AS', 'BAJA CALIFORNIA':'BC',
			'BAJA CALIFORNIA SUR':'BS', 'CAMPECHE':'CC', 'CHIAPAS':'CS',
			'CHIHUAHUA':'CH', 'COAHUILA':'CL', 'COLIMA':'CM', 'DISTRITO FEDERAL':'DF',
			'DURANGO':'DG', 'GUANAJUATO':'GT', 'GUERRERO':'GR', 'HIDALGO':'HG',
			'JALISCO':'JC', 'MEXICO':'MC', 'MICHOACAN':'MN', 'MORELOS':'MS',
			'NAYARIT':'NT', 'NUEVO LEON':'NL', 'OAXACA':'OC', 'PUEBLA':'PL',
			'QUERETARO':'QT', 'QUINTANA ROO':'QR', 'SAN LUIS POTOSI':'SP',
			'SINALOA':'SL', 'SONORA':'SR', 'TABASCO':'TC', 'TAMAULIPAS':'TS',
			'TLAXCALA':'TL', 'VERACRUZ':'VZ', 'YUCATÁN':'YN', 'ZACATECAS':'ZS',
			'NACIDO EXTRANJERO':'NE',
		}

		for key, value in estados.items():
			if key == param:
				estado = value
		
		return estado

	def consonante_curp(self, param):
		consonante = Utils().busca_consonante(param)
		return consonante

	def anio_fecha(self, fecha):
		anio = Utils().get_anio(fecha)
		return anio

import datetime
from utils import Utils

class BaseGenerator(object):

	def genera(self):
		raise NotImplementedError("No implemetado.")

	def parse(self, nombres, paterno, materno=None, estado=None):

		if estado != None:
			self.estado = Utils().upper(estado)

		if materno is not None:
			self.materno = Utils().upper(materno)
			self.materno = Utils().quita_articulo(self.materno)
			self.materno = Utils().quita_CH_LL(self.materno)

		self.nombres = Utils().upper(nombres)
		self.paterno = Utils().upper(paterno)
	
		self.nombres = Utils().quita_nombre(self.nombres)
		self.paterno = Utils().quita_articulo(self.paterno)

		self.nombres = Utils().quita_CH_LL(self.nombres)
		self.paterno = Utils().quita_CH_LL(self.paterno)
		

	def base_dato_fiscal(self, nombres, paterno, materno, fecha):
		# Regresa iniciales del nombre y verifica palabras 
		dato_fiscal = self.iniciales_nombre(nombres, paterno, materno)
		dato_fiscal = self.verifica_palabra(dato_fiscal)
		# Agrega fecha de nacimineto
		fecha_nacimiento = self.parse_fecha(fecha)
		dato_fiscal += fecha_nacimiento

		return dato_fiscal
		
	def iniciales_nombre(self, nombres, paterno, materno):
		iniciales = ''
		# Inicial del apellido paterno
		iniciales = paterno[0:1]
		# Busca la primera vocal del apellido paterno
		vocal = Utils().busca_vocal(paterno)
		# Agrega vocal
		iniciales += vocal 
		# inicial del apellido materno y nombre
		if materno is None:
			iniciales += 'X'
		else:
			iniciales += materno[0:1]
		iniciales += nombres[0:1]

		return iniciales

	def verifica_palabra(self, rfc):

		palabras = [ 
			'BUEI', 'BUEY', 'CACA', 'CACO', 'CAGA', 'CAGO', 'CAKA', 'CAKO', 'COGE',
			'COGI', 'COJA', 'COJE', 'COJI', 'COJO', 'COLA', 'CULO', 'FALO', 'FETO',
			'GETA', 'GUEI', 'GUEY', 'JETA', 'JOTO', 'KACA', 'KACO', 'KAGA', 'KAGO', 
			'KAKA', 'KAKO', 'KOGE', 'KOGI', 'KOJA', 'KOJE', 'KOJI', 'KOJO', 'KOLA', 
			'KULO', 'LILO', 'LOCA', 'LOCO', 'LOKA', 'LOKO', 'MAME', 'MAMO', 'MEAR', 
			'MEAS', 'MEON', 'MIAR', 'MION', 'MOCO', 'MOKO', 'MULA', 'MULO', 'NACA', 
			'NACO', 'PEDA', 'PEDO', 'PENE', 'PIPI', 'PITO', 'POPO', 'PUTA', 'PUTO', 
			'QULO', 'RATA', 'ROBA', 'ROBE', 'ROBO', 'RUIN', 'SENO', 'TETA', 'VUEI', 
			'VUEY', 'WUEI', 'WUEY',
		]

		for palabra in palabras:
			if palabra == rfc:
				rfc = "XXXX"
				break

		return rfc

	def parse_fecha(self, fecha):
		fecha_nac = ""
		fecha = datetime.datetime.strptime(fecha, '%d-%m-%Y').date()
		anio = str(fecha.year)
		anio = anio[2:4]
		# Rellena con ceros a la izquierda
		mes = str(fecha.month).zfill(2)
		dia = str(fecha.day).zfill(2)
		fecha_nac += anio+mes+dia 

		return fecha_nac


	def entidad_federativa(self, param):
		estado = None	
		estados = { 
			'':'', 'AGUASCALIENTES':'AS', 'BAJA CALIFORNIA':'BC',
			'BAJA CALIFORNIA SUR':'BS', 'CAMPECHE':'CC', 'CHIAPAS':'CS',
			'CHIHUAHUA':'CH', 'COAHUILA':'CL', 'COLIMA':'CM', 'DISTRITO FEDERAL':'DF',
			'DURANGO':'DG', 'GUANAJUATO':'GT', 'GUERRERO':'GR', 'HIDALGO':'HG',
			'JALISCO':'JC', 'MEXICO':'MC', 'MICHOACAN':'MN', 'MORELOS':'MS',
			'NAYARIT':'NT', 'NUEVO LEON':'NL', 'OAXACA':'OC', 'PUEBLA':'PL',
			'QUERETARO':'QT', 'QUINTANA ROO':'QR', 'SAN LUIS POTOSI':'SP',
			'SINALOA':'SL', 'SONORA':'SR', 'TABASCO':'TC', 'TAMAULIPAS':'TS',
			'TLAXCALA':'TL', 'VERACRUZ':'VZ', 'YUCATÁN':'YN', 'ZACATECAS':'ZS',
			'NACIDO EXTRANJERO':'NE',
		}

		for key, value in estados.items():
			if key == param:
				estado = value
		
		return estado

	def consonante_curp(self, param):
		consonante = Utils().busca_consonante(param)
		return consonante

	def anio_fecha(self, fecha):
		anio = Utils().get_anio(fecha)
		return anio
