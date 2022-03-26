# -*- coding: utf-8 -*-

def search_consonant(word):
	"""
	Consonant word search
	"""
	result = ''
	data = word[1:len(word)] if word else None
	for x in data:
		if x == 'Ñ':
			result = 'X'
			break
		elif get_consonant(x):
			result = x
			break
	return result


def get_consonant(data):
	"""Get consonants."""
	consonants = (
		'B', 'C', 'D',  'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
		'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
	)
	result = False
 
	for x in consonants:
		if x == data:
			result = True
			break
	return result


def search_vowel(last_name):
	"""Search for paternal surname vowel."""
	size = len(last_name)-1
	last_name = last_name[1:size]
	result = ''

	for x in last_name:
		if get_vocal(x):
			result = x
			break
	return result


def get_vocal(data):
	"""Get vocal."""
	vowels = ('A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú')
	result = False
 
	for x in vowels:
		if x == data:
			result = True
			break
	return result


def to_upper(text):
	"""Convert word to uppercase."""
	return text.upper().strip()
