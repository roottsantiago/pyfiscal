# -*- coding: utf-8 -*-
import datetime
import unicodedata

from .utils import (
	to_upper, search_vowel, search_consonant
)


class BaseGenerator(object):
	"""class Base Generator"""
	full_name = None
	first_name_master = None
	last_name_master = None
	mothers_last_name_master = None

	def generate(self):
		raise NotImplementedError('No implement.')

	def parse(self, complete_name, last_name, mother_last_name=None, city=None,
			  state_code=None):

		self.city = to_upper(city) if city else None
		self.state_code = to_upper(state_code) if state_code else None

		if mother_last_name:
			mother_last_name = self.remove_accents(to_upper(mother_last_name))
			self.mothers_last_name_master = mother_last_name
			mother_last_name = self.remove_articles(mother_last_name)
			mother_last_name = self.remove_precisions(mother_last_name)
			self.mother_last_name = mother_last_name

		first_name = self.remove_accents(to_upper(complete_name))
		self.first_name_master = first_name
		first_name = self.remove_names(first_name)
		first_name = self.remove_articles(first_name)
		first_name = self.remove_precisions(first_name)
		self.complete_name = first_name

		last_name = self.remove_accents(to_upper(last_name))
		self.last_name_master = last_name
		last_name = self.remove_articles(last_name)
		last_name = self.remove_precisions(last_name)
		self.last_name = last_name

		self.full_name = "{} {} {}".format(self.last_name_master, 
										   self.mothers_last_name_master, self.first_name_master)


	def data_fiscal(self, complete_name, last_name, mother_last_name, birth_date):
		birth_date = self.parse_date(birth_date)

		if len(last_name) == 1 or len(last_name) == 2:
			initials = self.initials_name_comp(complete_name, last_name, mother_last_name)
		elif mother_last_name == None or mother_last_name == '': #Rule 7
			initials = self.initials_single_last_name(complete_name, last_name)
		else:
			initials = self.initials_name(complete_name, last_name, mother_last_name)
		#Rule 9
		full_name_initials = self.verify_initials(initials)
		return "{0}{1}".format(full_name_initials, birth_date)
		
	
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

		initials = "{0}{1}{2}{3}".format(ini_last_name, last_name_vowel, 
										 ini_mothlast_name, ini_first_name)
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
			phrase = "C{}".format(data)
		elif letters == 'LL':
			phrase = "L{}".format(data)
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
		data = [
			'DE LA ',
			'DE LOS ',
			'DEL ',
   			'DE ',
			'LAS ',
			'LA ',
			'LOS ',
			'Y ',
			'MC ',
			'MAC ',
			'VON ',
			'VAN '
		]
		# Iterate over the strings to be replaced
		for elem in data:
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
		data = ['JOSE ', 'MARIA ']
		
		# Iterate over the strings to be replaced
		for elem in data :
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
		data = (
			('BUEI', 'BUEX'), ('BUEY', 'BUEX'), ('CACA', 'CACX'),
   			('CACO', 'CACX'), ('CAGA', 'CAGX'), ('CAGO', 'CAGX'),
			('CAKA', 'CAKX'), ('CAKO', 'CAKX'), ('COGE', 'COGX'),
			('COJA', 'COJX'), ('COJE', 'COJX'), ('COJI', 'COJX'),
			('COJO', 'COJX'), ('CULO', 'CULX'), ('FETO', 'FETX'),
			('GUEY', 'GUEX'), ('JOTO', 'JOTX'), ('KACA', 'KACX'),
			('KACO', 'KACX'), ('KAGA', 'KAGX'), ('KAGO', 'KAGX'),
			('KOGE', 'KOGX'), ('KOJO', 'KOJX'), ('KAKA', 'KAKX'),
			('KULO', 'KULX'), ('MAME', 'MAMX'), ('MAMO', 'MAMX'),
   			('MEAR', 'MEAX'), ('MEAS', 'MEAX'), ('MEON', 'MEOX'),
			('MION', 'MIOX'), ('MOCO', 'MOCX'), ('MULA', 'MULX'),
   			('PEDA', 'PEDX'), ('PEDO', 'PEDX'), ('PENE', 'PENX'),
			('PUTA', 'PUTX'), ('PUTO', 'PUTX'), ('QULO', 'QULX'),
			('RATA', 'RATX'), ('RUIN', 'RUIX'),
		)
		words = dict((x, y) for x, y in data)
		result = words.get(initials) if words.get(initials) else initials
		return result


	def remove_accents(self, text):
		""" Normalise (normalize) unicode data in Python to remove umlauts, accents etc.

		Rule 10 - When special characters appear as part of the name, paternal surname and maternal surname,
		they must be excluded for the calculation of the homonym and the verification digit. 
		The characters will be interpreted, yes and only if, they are individually within the name,
		paternal surname and maternal surname. Examples:
			
		Roberto O’farril Carballo OACR-661121
		Rubén D’angelo Fargo DAFR-710108
		Luz Ma. Fernández Juárez FEJL-830120
		"""		 
		#s_no_accents = ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
		try:
			text = unicode(text, 'utf-8')
		except (TypeError, NameError): # unicode is a default on python 3 
			pass
		text = unicodedata.normalize('NFD', text)
		text = text.encode('ascii', 'ignore')
		text = text.decode("utf-8")
		return str(text)


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
			return "{0}{1}{2}".format(year, month, day)
		except Exception as exc:
			raise str(exc)


	def city_search(self, name_city):
		entities = { 
			'': '',
			'AGUASCALIENTES': 'AS',
			'BAJA CALIFORNIA': 'BC',
			'BAJA CALIFORNIA SUR': 'BS',
			'CAMPECHE': 'CC',
			'CHIAPAS': 'CS',
			'CHIHUAHUA': 'CH',
			'COAHUILA': 'CL',
			'COLIMA': 'CM',
			'DISTRITO FEDERAL': 'DF',
			'DURANGO': 'DG',
			'GUANAJUATO': 'GT',
			'GUERRERO': 'GR',
			'HIDALGO': 'HG',
			'JALISCO': 'JC',
			'MEXICO': 'MC',
			'MICHOACAN': 'MN',
			'MORELOS': 'MS',
			'NAYARIT': 'NT',
			'NUEVO LEON':'NL',
			'OAXACA': 'OC',
			'PUEBLA': 'PL', 
			'QUERETARO': 'QT',
			'QUINTANA ROO': 'QR',
			'SAN LUIS POTOSI': 'SP',
			'SINALOA': 'SL',
			'SONORA': 'SR',
			'TABASCO': 'TC',
			'TAMAULIPAS': 'TS',
			'TLAXCALA': 'TL',
			'VERACRUZ': 'VZ',
			'YUCATÁN': 'YN',
			'ZACATECAS': 'ZS',
			'NACIDO EXTRANJERO': 'NE'
		}
		data = ''	
		for key, value in entities.items():
			if key == name_city:
				data = value
				break
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
		