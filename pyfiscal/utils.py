# -*- coding: utf-8 -*-

ENT_FED = { 
	'': '', 'AGUASCALIENTES': 'AS', 'BAJA CALIFORNIA': 'BC', 'BAJA CALIFORNIA SUR': 'BS',
	'CAMPECHE': 'CC', 'CHIAPAS': 'CS', 'CHIHUAHUA': 'CH', 'COAHUILA': 'CL', 'COLIMA': 'CM',
	'DISTRITO FEDERAL': 'DF', 'DURANGO': 'DG', 'GUANAJUATO': 'GT', 'GUERRERO': 'GR',
	'HIDALGO': 'HG', 'JALISCO': 'JC', 'MEXICO': 'MC', 'MICHOACAN': 'MN', 'MORELOS': 'MS',
	'NAYARIT': 'NT', 'NUEVO LEON':'NL', 'OAXACA': 'OC', 'PUEBLA': 'PL', 'QUERETARO': 'QT',
	'QUINTANA ROO': 'QR', 'SAN LUIS POTOSI': 'SP', 'SINALOA': 'SL', 'SONORA': 'SR',
	'TABASCO': 'TC', 'TAMAULIPAS': 'TS', 'TLAXCALA': 'TL', 'VERACRUZ': 'VZ', 'YUCATÁN': 'YN',
	'ZACATECAS': 'ZS', 'NACIDO EXTRANJERO': 'NE'
}

DISADVANTAGES_WORDS = (
	('BUEI', 'BUEX'), ('BUEY', 'BUEX'),
	('CACA', 'CACX'), ('CACO', 'CACX'),
	('CAGA', 'CAGX'), ('CAGO', 'CAGX'),
	('CAKA', 'CAKX'), ('CAKO', 'CAKX'),
	('COGE', 'COGX'), ('COJA', 'COJX'),
	('COJE', 'COJX'), ('COJI', 'COJX'),
	('COJO', 'COJX'), ('CULO', 'CULX'),
	('FETO', 'FETX'), ('GUEY', 'GUEX'),
	('JOTO', 'JOTX'), ('KACA', 'KACX'),
	('KACO', 'KACX'), ('KAGA', 'KAGX'),
	('KAGO', 'KAGX'), ('KOGE', 'KOGX'),
	('KOJO', 'KOJX'), ('KAKA', 'KAKX'),
	('KULO', 'KULX'), ('MAME', 'MAMX'),
	('MAMO', 'MAMX'), ('MEAR', 'MEAX'),
	('MEAS', 'MEAX'), ('MEON', 'MEOX'),
	('MION', 'MIOX'), ('MOCO', 'MOCX'),
	('MULA', 'MULX'), ('PEDA', 'PEDX'),
	('PEDO', 'PEDX'), ('PENE', 'PENX'),
	('PUTA', 'PUTX'), ('PUTO', 'PUTX'),
	('QULO', 'QULX'), ('RATA', 'RATX'),
	('RUIN', 'RUIX')
)


def search_consonant(word):
	data = None
	consonant = ''
	length = 0

	if word:
		data = word[1:len(word)]

	for item in data:
		if item == 'Ñ':
			consonant = 'X'
			break
		elif get_consonant(item):
			consonant = item
			break
	return consonant

def get_consonant(consonant):
	"""
	Consonants.
	"""
	consonants = (
		'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
		'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
	)

	for item in consonants:
		if item == consonant:
			return True
			break
	return False

def search_vowel(last_name):
	"Search for paternal surname vowel."
	size = len(last_name) - 1
	last_name = last_name[1:size]

	vocal = ''
	for v in last_name:
		if get_vocal(vocal=v):
			vocal = v
			break
	return vocal

def get_vocal(vocal):
	"Get vocal."
	vowels = ('A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú')

	for v in vowels:
		if v == vocal:
			return True
			break
	return False
			
def to_upper(text):
	"Convert word to uppercase."
	word = text.upper()
	return word.strip()

