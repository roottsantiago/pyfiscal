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

	def consonate_curp(self, palabra):

		Len = 0
		valor = ''
		Len = len(palabra)
		Len = Len - 1;

		if Len < 0:
			Len = 1

		# Identificar si la palabra empieza con una consonante
		letra = palabra[0:1]
		for item in letra:
			if self.es_consonante(item):
				consonante1 = item
				break
		
		valor = palabra
		if consonante1 != '':
			valor = palabra[1:Len]

		#Buscamos y agregamos al rfc la primera vocal del primer apellido
		for item in valor:
			val = item
			if val == "Ñ":
				consonante = ''
				break
			elif self.es_consonante(item):
				consonante = item
				break
		
		return consonante

	def es_consonante(self, param):
		consonantes = (
			'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
			'T', 'V', 'W', 'X', 'Y', 'Z'
		)

		for consonante in consonantes:
			if consonante == param:
				return True
				break

		return False

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
