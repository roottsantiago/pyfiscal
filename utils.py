import datetime
class utils:
	
	def quitaArticulo(param):
		str_empty = ""
		return param.replace("DE ", str_empty).replace("DEL ", str_empty).replace("LA ", str_empty).replace("LOS ", str_empty).replace("LAS ", str_empty).replace("Y ", str_empty).replace("MC ", str_empty).replace("MAC ", str_empty).replace("VON ", str_empty).replace("VAN ", str_empty)

	def quitaNombre(param):
		str_empty = ""
		return param.replace("JOSE ", str_empty).replace("J ", str_empty).replace("J. ", str_empty).replace("MARIA ", str_empty).replace("MA. ", str_empty).replace("MA ", str_empty).replace("DE ", str_empty).replace(" DE ", str_empty).replace("DEL ", str_empty).replace(" DEL ", str_empty).replace("LA ", str_empty).replace(" LA ", str_empty).replace("LAS ", str_empty).replace(" LAS ", str_empty).replace("LOS ", str_empty).replace(" LOS ", str_empty).replace("MC ", str_empty).replace("MAC ", str_empty).replace("VON ", str_empty).replace("VAN ", str_empty).replace(" Y ", str_empty);

	def quitarCHLL(palabra):
		if palabra !="":
			if palabra[0:2] == "CH":
				palabra = "C" + palabra[2:len(palabra)-2]
			elif palabra[0:2] == "LL":
				palabra = "L" + palabra[2:len(palabra)-2]
		return palabra

	def getConsonate(palabra):
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
			if utils.EsConsonante(item):
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
			elif utils.EsConsonante(item):
				consonante = item;
				break
		
		return consonante

	def EsConsonante(letra):
		consonante = False
		array_con = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
		count = 0
		for con in array_con:
			count += 1
			if con == letra:
				consonante = True
				break
		return consonante;

	def esVocal(letra):
		#Aunque para el caso del RFC cambié todas las letras a mayúsculas igual agregé las minúsculas.
		if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' or letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
			return True;
		else:
			return False

	def calculaOrigenCurp(nombre, apellidoPaterno, apellidoMaterno):
		rfc = "";
		# No tiene Apellido Paterno
		if apellidoPaterno == "" and apellidoMaterno != "":
			#Agregamos el primer caracter del apellido paterno
			rfc = "XX";
			rfc += apellidoMaterno[0:2]

		# No tiene Apellido Materno 
		if apellidoMaterno == "" and apellidoPaterno != "":
			#Agregamos el primer caracter del apellido paterno
			rfc = apellidoPaterno[0:1]
			z1 = len(apellidoPaterno) - 1;
			apePaterno = apellidoPaterno[1:z1]
			#Buscamos y agregamos al rfc la primera vocal del apellido
			for item in apePaterno:
				if utils.esVocal(item):
					rfc += item
					break

			rfc += "X"
			#Armar letras del nombre
			rfc += nombre[0:1]

		if apellidoPaterno != "" and apellidoMaterno != "":
			#Agregamos el primer caracter del apellido paterno
			rfc = apellidoPaterno[0:1]
			z1 = len(apellidoPaterno) - 1
			apePaterno = apellidoPaterno[1:z1]

           #Buscamos y agregamos al rfc la primera vocal del primer apellido
			for item in apePaterno:
				if utils.esVocal(item):
					rfc += item
					break
			rfc += apellidoMaterno[0:1]
			 #Agregamos el primer caracter del primer nombre
			rfc += nombre[0:1]

		return rfc


	def verificarPalabras(rfc, origen):
		lstPalabras = [ "BUEI", "BUEY", "CACA", "CACO", "CAGA", "CAGO", "CAKA", "CAKO", "COGE", "COGI", "COJA", "COJE", "COJI", "COJO", "COLA", "CULO", "FALO", "FETO",
				"GETA", "GUEI", "GUEY","JETA", "JOTO", "KACA", "KACO", "KAGA", "KAGO", "KAKA", "KAKO", "KOGE", "KOGI", "KOJA", "KOJE", "KOJI", "KOJO", "KOLA", "KULO",
				"LILO", "LOCA", "LOCO", "LOKA", "LOKO", "MAME", "MAMO", "MEAR", "MEAS", "MEON", "MIAR", "MION", "MOCO", "MOKO", "MULA", "MULO", "NACA", "NACO", "PEDA", 
				"PEDO", "PENE", "PIPI", "PITO", "POPO", "PUTA", "PUTO", "QULO", "RATA", "ROBA", "ROBE", "ROBO", "RUIN", "SENO", "TETA", "VUEI", "VUEY", "WUEI", "WUEY",
			]

		count = 0
		for palabra in lstPalabras:
			count += 1
			if palabra == rfc:
				if origen == "RFC":
					rfc = rfc[0:3] + "X"
				elif origen == "CURP":	
					rfc = rfc[0:1] + "X" + rfc[2:2];
					break

		return rfc

	def fechaNacimiento(rfc, fechaNac):
		# Convertir str a Date
		fecha_nac = datetime.datetime.strptime(fechaNac, '%d-%m-%Y').date()
		anio = fecha_nac.year
		mes = fecha_nac.month
		dia = fecha_nac.day
		# Quitar primeros 2 digitos del año
		str_anio = str(anio)
		str_anio = str_anio[2:4]
		# Agregar anio, mes y dia
		rfc += str_anio + str(mes) + str(dia)
		return rfc
