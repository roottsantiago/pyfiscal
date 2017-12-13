# -*- coding: utf-8 -*-
import datetime
from utils import Utils
from constants import ENT_FED, WORDS

util = Utils()


class BaseGenerator(object):
	"""class Base"""
	def generate(self):
		raise NotImplementedError('No implement.')

	def parse(self, nombres, paterno, materno=None, city=None, state_code=None):
		if city is not None:
			self.city = util.upper(city)
		if state_code is not None:
			self.state_code = util.upper(state_code)
		if materno is not None:
			self.materno = util.upper(materno)
			self.materno = util.remove_article(self.materno)
			self.materno = util.remove_precisions(self.materno)
		self.nombres = util.upper(nombres)
		self.nombres = util.remove_names(self.nombres)
		self.nombres = util.remove_precisions(self.nombres)
		self.paterno = util.upper(paterno)
		self.paterno = util.remove_article(self.paterno)
		self.paterno = util.remove_precisions(self.paterno)
		
	def data_fiscal(self, nombres, paterno, materno, fecha):
		initials = self.initials_name(nombres, paterno, materno)
		data = self.verify_words(initials)
		# Add date of birth.
		data += self.parse_date(fecha)
		return data
		
	def initials_name(self, nombres, paterno, materno):
		iniciales = ''
		# Inicial del apellido paterno
		iniciales = paterno[0:1]
		# Busca la primera vocal del apellido paterno
		vocal = util.search_vowel(paterno)
		# Agrega vocal
		iniciales += vocal 
		# inicial del apellido materno y nombre
		if materno is None:
			iniciales += 'X'
		else:
			iniciales += materno[0:1]
		iniciales += nombres[0:1]

		return iniciales

	def verify_words(self, rfc):
		for item in WORDS:
			if item == rfc:
				rfc = 'XXXX'
				break

		return rfc

	def parse_date(self, fecha):
		fecha_nac = ''
		fecha_type = type(fecha)

		if fecha is None:
			fecha = datetime.datetime.today()
		else:
			if not (fecha_type is datetime.datetime or fecha_type is datetime.date):
				fecha = datetime.datetime.strptime(fecha, '%d-%m-%Y').date()
		
		anio = str(fecha.year)
		anio = anio[2:4]
		# Fill with zeros to the left.
		mes = str(fecha.month).zfill(2)
		dia = str(fecha.day).zfill(2)
		fecha_nac += anio + mes + dia 

		return fecha_nac

	def entidad_federativa(self, ent_fed):
		data = ''	
		for key, value in ENT_FED.items():
			if key == ent_fed:
				data = value
		
		return data

	def consonante_curp(self, word):
		return util.search_consonant(word)

	def get_year(self, str_date):
		return util.get_year(str_date)
