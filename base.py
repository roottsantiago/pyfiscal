# -*- coding: utf-8 -*-
import datetime
from utils import Utils
from constants import ENT_FED, WORDS

util = Utils()


class BaseGenerator(object):
	"""class Base"""
	def generate(self):
		raise NotImplementedError('No implement.')

	def parse(self, complete_name, last_name, mother_last_name=None, city=None, state_code=None):
		if city is not None:
			self.city = util.upper(city)
		if state_code is not None:
			self.state_code = util.upper(state_code)
		if mother_last_name is not None:
			self.mother_last_name = util.upper(mother_last_name)
			self.mother_last_name = util.remove_article(self.mother_last_name)
			self.mother_last_name = util.remove_precisions(self.mother_last_name)
		self.complete_name = util.upper(complete_name)
		self.complete_name = util.remove_names(self.complete_name)
		self.complete_name = util.remove_precisions(self.complete_name)
		self.last_name = util.upper(last_name)
		self.last_name = util.remove_article(self.last_name)
		self.last_name = util.remove_precisions(self.last_name)
		
	def data_fiscal(self, complete_name, last_name, mother_last_name, birth_date):
		initials = self.initials_name(complete_name, last_name, mother_last_name)
		data = self.verify_words(initials)
		# Add date of birth.
		data += self.parse_date(birth_date)
		return data
		
	def initials_name(self, complete_name, last_name, mother_last_name):
		iniciales = ''
		# Inicial del apellido paterno
		iniciales = last_name[0:1]
		# Busca la primera vocal del apellido paterno
		vocal = util.search_vowel(last_name)
		# Agrega vocal
		iniciales += vocal 
		# inicial del apellido mother_last_name y nombre
		if mother_last_name is None:
			iniciales += 'X'
		else:
			iniciales += mother_last_name[0:1]
		iniciales += complete_name[0:1]

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
