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

	def getConsonateCurp(palabra):
		consonante = ""
		Len = 0
		valor = ""
		Len = len(palabra)
		Len = Len - 1;

		if Len < 0:
			Len = 1
		# Identificar si la palabra empieza con una consonante
		consonante1 = "";
		letra = palabra[0:1]

		for item in letra:
			if Utils.esConsonante(item):
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
			elif Utils.esConsonante(item):
				consonante = item;
				break
		
		return consonante

	def esConsonante(letra):
		consonante = False
		array_con = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
		count = 0
		for con in array_con:
			count += 1
			if con == letra:
				consonante = True
				break
		return consonante

	def esVocal(letra):
		#Aunque para el caso del RFC cambié todas las letras a mayúsculas igual agregé las minúsculas.
		if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' or letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
			return True;
		else:
			return False
			
	def anioFecha(fechaNac):
		fecha_nac = datetime.datetime.strptime(fechaNac, '%d-%m-%Y').date()
		anio = fecha_nac.year
		return anio

	def rfcSet(a, b):
		if a == b:
			return b
		else :
			return a

	def upper(self, texto):
		palabra = None
		palabra = texto.upper()
		palabra	= palabra.strip()

		return palabra
