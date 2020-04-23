# -*- coding: utf-8 -*-
import datetime
from .utils import (
	ENT_FED, DISADVANTAGES_WORDS, to_upper,
	search_vowel, search_consonant
)


class BaseGenerator(object):
	"""class Base Generator"""
	def generate(self):
		raise NotImplementedError('No implement.')

	def parse(self, complete_name, last_name, mother_last_name=None, city=None,
		state_code=None):
		if city is not None:
			self.city = to_upper(city)
		if state_code is not None:
			self.state_code = to_upper(state_code)
		if mother_last_name is not None:
			self.mother_last_name = to_upper(mother_last_name)
		self.complete_name = to_upper(complete_name)
		self.last_name = to_upper(last_name)
		
	def data_fiscal(self, complete_name, last_name, mother_last_name, birth_date):
		birth_date = self.parse_date(birth_date)

		first_name = self.remove_precisions(self.complete_name)
		last_name = self.remove_precisions(self.last_name)

		if mother_last_name is not None:
			mother_last_name = self.remove_precisions(self.mother_last_name)
			mother_last_name = self.remove_articles(self.mother_last_name)

		#Rule 6
		first_name = self.remove_names(first_name)
		# Rule 8
		last_name = self.remove_articles(last_name)
		
		if len(last_name) is 1 or len(last_name) is 2:
			initials = self.initials_name_comp(first_name, last_name, mother_last_name)
		elif mother_last_name is None or mother_last_name is '': #Rule 7
			initials = self.initials_single_last_name(first_name, last_name)
		else:
			initials = self.initials_name(first_name, last_name, mother_last_name)
		#Rule 9
		completename = self.verify_initials(initials)
		
		return '%s%s' % (completename, birth_date)
		
	def initials_name(self, first_name, last_name, mother_last_name):
		"""Rule 1 - The key is integrated with the following data:

		1.- The first letter of the father's last name and the next first vowel of the same.
		2.- The first letter of the mother's last name.
		3.- The first letter of the name.
		"""
		
		ini_last_name = last_name[0:1]
		last_name_vowel = search_vowel(last_name)
		ini_mothlast_name = self.get_ini_mothlast_name(mother_last_name)
		ini_first_name = first_name[0:1]

		# Rule 5
		# When the paternal or maternal surname are composed, the first word that corresponds
		# to any of them will be taken for the classification.
		# Dolores San Martín Dávalos SADD-180812
		# Mario Sánchez de la Barquera Gómez SAGM-190224
		# Antonio Jiménez Ponce de León JIPA-170808

		initials = '%s%s%s%s' % (
			ini_last_name, 
			last_name_vowel, 
			ini_mothlast_name, 
			ini_first_name
		)
		return initials

	
	def remove_precisions(self, phrase):
		""" Rule 3 - When the initial letter of any of the surnames or first names is composed,
		only its initial will be noted. In Ch la C and in Ll la L.

		For example:
			Manuel Chávez González CAGM-240618
			Felipe Camargo Llamas CALF-450228
			Charles Kennedy Truman KETC-511012
		"""
		letters = phrase[0:2]
		data = phrase[2:len(phrase)]
		
		if letters == 'CH':
			phrase = 'C%s' % data
		elif letters == 'LL':
			phrase = 'L%s' % data
		return phrase


	def remove_articles(self, phrase):
		"""
		Replace all the occurrences of string in list.

		Rule 8 - When articles, prepositions, conjunctions or contractions appear
		in the name of natural persons, they will not be taken as elements of integration of the code,
		examples:
			Carmen de la Peña Ramírez PERC-631201
			Mario Sánchez de los Cobos SACM-701110
			Roberto González and Durán GODR-600101
			Juan del Valle Martínez VAMJ-691001
		"""
		to_replaces = ['DE LA', 'DE LOS', 'DEL', 'DE', 'LAS', 'LA', 'LOS', 'Y', 'MC', 'MAC', 'VON', 'VAN']
		# Iterate over the strings to be replaced
		for elem in to_replaces :
			# Check if string is in the main string
			if elem in phrase:
				# Replace the string
				phrase = phrase.replace(elem, '').strip()
		return phrase 


	def remove_names(self, first_name):
		""" Rule 6 - When the name is composed, that is, it is made up of two or more words,
		the initial letter of the first will be taken for the conformation, 
		provided it is not MARIA or JOSE given its frequent use, 
		in which case the first letter will be taken of the second word.
		
		For example:
			Luz María Fernández Juárez FEJL-200205
			José Antonio Camargo Hernández CAHA-211218
			María Luisa Ramírez Sánchez RASL-251112
		"""
		to_replaces = ['JOSE', 'MARIA']
		
		# Iterate over the strings to be replaced
		for elem in to_replaces :
			# Check if string is in the main string
			if elem in first_name :
				# Replace the string
				first_name = first_name.replace(elem, '').strip()
		return first_name 


	def get_ini_mothlast_name(self, mother_last_name):
		"""	The first letter of the mother's last name.
		"""
		return mother_last_name[0:1] if mother_last_name else ''


	def initials_name_comp(self, first_name, last_name, mother_last_name):
		"""Rule 4 - In cases where the paternal surname of the natural person
			is made up of one or two letters, the password will be formed as follows:

			1.- The first letter of the paternal surname.
			2.- The first letter of the mother's last name.
			3.- The first and second letters of the name.

		For example:
			Alvaro de la O Lozano 	OLAL-401201
			Ernesto Ek Rivera 	ERER-071120
		"""
		ini_last_name = last_name[0:1]
		ini_mthlast_name = self.get_ini_mothlast_name(mother_last_name)
		data = "{}{}{}".format(ini_last_name, ini_mthlast_name, first_name[0:2])
	 	return data  


	def initials_single_last_name(self, first_name, last_name):
		"""Rule 7 - In the cases in which the natural person has only one surname,
		he will comply with the first and second letters of the paternal or maternal surname, 
		as it appears on the birth certificate, plus the first and second letters of the name.

		For example:
		Juan Martínez MAJU-420116
		Gerarda Zafra ZAGE-251115
		"""
		return '{}{}'.format(last_name[0:2], first_name[0:2], )


	def verify_initials(self, initials):
		"""
		Rule 9 - When an inconvenient word appears from the four letters that make up
		the alphabetical expression, the last letter will be replaced by an "X".
		"""
		words = dict((x, y) for x, y in DISADVANTAGES_WORDS)
		data = words.get(initials) if words.get(initials) else initials
		return data


	def parse_date(self, birthdate):
		"""Rule 2 - The taxpayer's date of birth will be noted below, in the following order:

		1. Year: The last two figures will be taken, writing them in Arabic numerals.
		2.- Month: The month of birth will be taken in its order number, in a calendar year,
			writing it with Arabic numbers.
		3.- Day: It will be written in Arabic numerals.

		Args:
			birthdate: The first parameter.

		Returns:
		As a result we will have the numerical expression: 070401
		"""
		try:
			dtype = type(birthdate)
			if birthdate is None:
				birthdate = datetime.datetime.today()
			else:
				if not (dtype is datetime.datetime or dtype is datetime.date):
					birthdate = datetime.datetime.strptime(birthdate, '%d-%m-%Y').date()
			
			year = str(birthdate.year)
			year = year[2:4]
			# When in the year, month or day, of the date of birth, only one figure appears,
			# a ZERO will be put before it.
			month = str(birthdate.month).zfill(2)
			day = str(birthdate.day).zfill(2)
			return '%s%s%s' % (year, month, day)
		except Exception as exc:
			raise str(exc)

	def city_search(self, name_city):
		data = ''	
		for key, value in ENT_FED.items():
			if key == name_city:
				data = value
		return data

	def get_consonante(self, word):
		return search_consonant(word)

	def get_year(self, str_date):
		"""Get year of birth date."""
		try:
			if str_date is None:
				date = datetime.datetime.today()
			else:
				date = datetime.datetime.strptime(str_date, '%d-%m-%Y').date()
			return date.year
		except Exception as exc:
			raise str(exc)

	def current_year(self):
		return datetime.datetime.now().year
		