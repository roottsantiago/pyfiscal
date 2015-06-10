import datetime


class Utils(object):
	
	def quita_articulo(self, param):
		str_empty = ""
		return param.replace("DE ", str_empty).replace("DEL ", str_empty).replace("LA ", str_empty).replace("LOS ", str_empty).replace("LAS ", str_empty).replace("Y ", str_empty).replace("MC ", str_empty).replace("MAC ", str_empty).replace("VON ", str_empty).replace("VAN ", str_empty)

	def quita_nombre(self, param):
		str_empty = ""
		return param.replace("JOSE ", str_empty).replace("J ", str_empty).replace("J. ", str_empty).replace("MARIA ", str_empty).replace("MA. ", str_empty).replace("MA ", str_empty).replace("DE ", str_empty).replace(" DE ", str_empty).replace("DEL ", str_empty).replace(" DEL ", str_empty).replace("LA ", str_empty).replace(" LA ", str_empty).replace("LAS ", str_empty).replace(" LAS ", str_empty).replace("LOS ", str_empty).replace(" LOS ", str_empty).replace("MC ", str_empty).replace("MAC ", str_empty).replace("VON ", str_empty).replace("VAN ", str_empty).replace(" Y ", str_empty);

	def quita_CH_LL(self, palabra):
		if palabra !="":
			if palabra[0:2] == "CH":
				palabra = "C" + palabra[2:len(palabra)-2]
			elif palabra[0:2] == "LL":
				palabra = "L" + palabra[2:len(palabra)-2]
		return palabra

	def consonate_curp(self, palabra):
		Len = 0
		valor = ""
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
		if consonante1 != "":
			valor = palabra[1:Len]

		#Buscamos y agregamos al rfc la primera vocal del primer apellido
		for item in valor:
			val = item
			if val == "Ñ":
				consonante = "";
				break
			elif self.es_consonante(item):
				consonante = item;
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
