# -*- coding: utf-8 -*-

import datetime


class Utils(object):
	
	def quita_articulo(self, article):
		"Remove article."
		articles = (
			'DE ', 'DEL ', 'LA ', 'LOS ', 'LAS ', 'Y ', 'MC ', 'MAC ', 'VON ', 'VAN '
		)
		
		for item in articles:
			data = article.replace(item, '')
		return data

	def quita_nombre(self, name):
		"Remove defined names in the tuple."
		names = ('JOSE ','J ', 'MARIA ', 'MA. ', 'DE ', ' DE ', 'DEL ', ' DEL ', 'LA ', ' LA ',
				 'LAS ', ' LAS ', 'LOS ', ' LOS ', 'MC ', 'MC ', 'MAC ', 'VON ', 'VAN ', ' Y ')
		
		for item in names:
			data = name.replace(item, '')
		return data

	def quita_CH_LL(self, text):
		letters = text[0:2]
		data = text[2:len(text)]
		
		if letters == "CH":
			text = "C%s" % data
		elif letters == "LL":
			text = "L%s" % data
		return text

	def busca_consonante(self, word):
		data = 'X'
		consonant = ''
		length = 0

		if word:
			length = len(word)
			length = length-1
			data = word[1:length]

		for item in data:
			if item == "Ñ":
				consonant = 'X'
				break
			elif self.consonante(item):
				consonant = item
				break
		return consonant

	def consonante(self, consonant):
		"Get consonant."
		consonants = ('B', 'C', 'D','F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
					  'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z')

		for item in consonants:
			if item == consonant:
				return True
				break
		return False

	def busca_vocal(self, last_name):
		"Search for paternal surname vowel."
		size = len(last_name) - 1
		last_name = last_name[1:size]

		for vocal in last_name:
			if self.vocal(vocal=vocal):
				data = vocal
				break
		return data

	def vocal(self, vocal):
		"Get vocal."
		vowels = ('A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú')

		for item in vowels:
			item = vocal
			return True
			break
		return False
			
	def upper(self, text):
		"Convert word to uppercase."
		word = text.upper()
		return word.strip()

	def get_year(self, str_date):
		"Get year of birth date."
		try:
			date = datetime.datetime.strptime(str_date, '%d-%m-%Y').date()
			return date.year
		except Exception as exc:
			raise str(exc)
