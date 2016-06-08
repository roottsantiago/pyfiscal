# -*- coding: utf-8 -*-

import datetime


class Utils(object):
	
	def quita_articulo(self, param):
		remplazar = ''
		buscar = (
			'DE ', 'DEL ', 'LA ', 'LOS ', 'LAS ','Y ', 'MC ', 'MAC ', 'VON ',
			'VAN '
		)
		
		reemplazado = param
		for articulo in buscar:
			reemplazado = reemplazado.replace(articulo, remplazar)
		return reemplazado

	def quita_nombre(self, param):
		remplazar = ''
		buscar = (
			'JOSE ', 'J ', 'MARIA ', 'MA. ', 'DE ', ' DE ', 'DEL ', ' DEL ', 'LA ',
			' LA ', 'LAS ', ' LAS ', 'LOS ', ' LOS ', 'MC ', 'MC ', 'MAC ', 'VON ',
			'VAN ', ' Y '
		)
		
		reemplazado = param
		for articulo in buscar:
			reemplazado = reemplazado.replace(articulo, remplazar)
		return reemplazado

	def quita_CH_LL(self, texto):
		letras = texto[0:2]
		concatenar = texto[2:len(texto)]
		
		if letras == "CH":
			texto = "C%s" % concatenar
		elif letras == "LL":
			texto = "L%s" % concatenar
		return texto

	def busca_consonante(self, palabra):
		valor = ''
		consonante = ''
		longitud = 0
		# Validar si no es null
		if palabra is not None:
			longitud = len(palabra)
			longitud = longitud-1
			valor = palabra[1:longitud]
		else:
			valor = 'X'

		for letra in valor:
			if letra == "Ñ":
				consonante = 'X'
				break
			elif self.consonante(letra):
				consonante = letra
				break
		return consonante

	def consonante(self, param):
		consonantes = (
			'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
			'T', 'V', 'W', 'X', 'Y', 'Z'
		)

		for consonante in consonantes:
			if consonante == param:
				return True
				break
		return False

	def busca_vocal(self, paterno):
		size = len(paterno)-1
		paterno = paterno[1:size]

		for letra in paterno:
			if self.vocal(letra):
				vocal = letra
				break
		return vocal

	def vocal(self, param):
		vocales = ("A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú")

		for vocal in vocales:
			vocal = param
			return True
			break
		return False
			
	def upper(self, texto):
		palabra = texto.upper()
		palabra	= palabra.strip()
		return palabra

	def anio(self, fecha):
		fecha = datetime.datetime.strptime(fecha, '%d-%m-%Y').date()
		anio = fecha.year
		return anio
