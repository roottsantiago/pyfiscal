# -*- coding: utf-8 -*-
from .constants import (
	VOWELS, CONSONANTS
)


def search_consonant(word):
	data = None
	consonant = ''

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
	"""Get consonants."""
	for i in CONSONANTS:
		if i == consonant:
			return True
			break
	return False


def search_vowel(last_name):
	"""Search for paternal surname vowel."""
	size = len(last_name)-1
	last_name = last_name[1:size]
	vocal = ''

	for v in last_name:
		if get_vocal(v):
			vocal = v
			break
	return vocal


def get_vocal(v):
	"""Get vocal."""
	for i in VOWELS:
		if i == v:
			return True
			break
	return False


def to_upper(text):
	"""Convert word to uppercase."""
	return text.upper().strip()
