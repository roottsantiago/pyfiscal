# -*- coding: utf-8 -*-
from base import BaseGenerator

import unicodedata


class CalculeRFC(BaseGenerator):
	key_value = 'rfc'
	DATA_REQUIRED = ('complete_name', 'last_name', 'mother_last_name', 'birth_date')
	partial_data = None

	def __init__(self, **kwargs):
		self.complete_name = kwargs.get('complete_name')
		self.last_name = kwargs.get('last_name')
		self.mother_last_name = kwargs.get('mother_last_name')
		self.birth_date = kwargs.get('birth_date')

		self.parse(complete_name=self.complete_name, last_name=self.last_name, 
				  mother_last_name=self.mother_last_name)
		
		self.partial_data = self.data_fiscal(
			complete_name=self.complete_name, last_name=self.last_name, 
			mother_last_name=self.mother_last_name, birth_date=self.birth_date)

	def genera(self):
		if self.mother_last_name is not None:
			nombrecompleto = u"%s %s %s" % (self.last_name, self.mother_last_name, self.complete_name)
		else:
			nombrecompleto = u"%s %s" % (self.last_name, self.complete_name)

		# Cálcula y agrega homoclave al RFC
		rfc = self.partial_data
		homoclave = self.homoclave_rfc(self.partial_data, nombrecompleto)
		rfc += homoclave
		# Cálcula y agrega digito verificador al RFC
		digito = self.numero_verificador(rfc)
		rfc += digito

		return rfc

	def remover_accentos(self, s):
		if type(s) is str:
			s = u"%s" % s
		return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

	def homoclave_rfc(self, rfc, nombrecompleto):
		nombre_numero = "0"
		suma_valor = 0 
		div = 0 
		mod = 0

		rfc1 = {
			" ":00, "&":10, "Ñ":10, "A":11, "B":12, "C":13, "D":14, "E":15, "F":16,
			"G":17, "H":18, "I":19, "J":21, "K":22, "L":23, "M":24, "N":25, "O":26,
			"P":27, "Q":28, "R":29, "S":32, "T":33, "U":34, "V":35, "W":36, "X":37,
			"Y":38, "Z":39, "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,
			"8":8,"9":9,
		}
		rfc2 = {
			0:"1", 1:"2", 2:"3", 3:"4", 4:"5", 5:"6", 6:"7", 7:"8", 8:"9", 9:"A", 10:"B",
			11:"C", 12:"D", 13:"E", 14:"F", 15:"G", 16:"H", 17:"I", 18:"J", 19:"K",
			20:"L", 21:"M", 22:"N", 23:"P", 24:"Q", 25:"R", 26:"S", 27:"T", 28:"U",
			29:"V", 30:"W", 31:"X", 32:"Y",
		}

		# Recorrer el nombre y convertir las letras en su valor numérico.
		for count in range(0, len(nombrecompleto)):
			letra = self.remover_accentos(nombrecompleto[count])

			nombre_numero += self.rfc_set(str(rfc1[letra]),"00")
		# La formula es:
            # El caracter actual multiplicado por diez mas el valor del caracter
            # siguiente y lo anterior multiplicado por el valor del caracter siguiente.
		for count in range(0,len(nombre_numero)-1):
			count2 = count+1
			suma_valor += ((int(nombre_numero[count])*10) + int(nombre_numero[count2])) * int(nombre_numero[count2])
		
		div = suma_valor % 1000
		mod = div % 34
		div = (div-mod)/34
		homoclave = ""
		homoclave += self.rfc_set(rfc2[int(div)],"Z")
		homoclave += self.rfc_set(rfc2[int(mod)],"Z")
		return homoclave

	def numero_verificador(self, rfc):
		suma_numero = 0 
		suma_parcial = 0
		digito = None 

		rfc3 = {
			"A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18,
			"J":19, "K":20, "L":21, "M":22, "N":23, "O":25, "P":26, "Q":27, "R":28,
			"S":29, "T":30, "U":31, "V":32, "W":33, "X":34, "Y":35, "Z":36, "0":0,
			"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "":24,
			" ":37,
		}

		for count in range(0,len(rfc)):
			letra = rfc[count]
			if rfc3[letra]:
				suma_numero = rfc3[letra]
				suma_parcial += (suma_numero*(14-(count+1)))

		modulo = suma_parcial % 11
		digito_parcial = (11-modulo)
		
		if modulo == 0:
			digito = "0"
		if digito_parcial == 10:
			digito = "A"
		else:
			digito = str(digito_parcial)

		return  digito

	def rfc_set(self, a, b):
		if a == b:
			return b
		else:
			return a


	@property
	def data(self):
		return self.genera()


class CalculeCURP(BaseGenerator):
	""" Calculer CURP"""
	key_value = 'curp'
	partial_data = None
	DATA_REQUIRED = (
		'complete_name',
		'last_name',
		'mother_last_name',
		'birth_date',
		'gender',
		'city',
		'state_code'
	)
	
	def __init__(self, **kwargs):
		self.complete_name = kwargs.get('complete_name')
		self.last_name = kwargs.get('last_name')
		self.mother_last_name = kwargs.get('mother_last_name', None)
		self.birth_date = kwargs.get('birth_date')
		self.gender = kwargs.get('gender')
		self.city = kwargs.get('city', None)
		self.state_code = kwargs.get('state_code', None)

		self.parse(complete_name=self.complete_name, last_name=self.last_name, mother_last_name=self.mother_last_name,
				   city=self.city, state_code=self.state_code)

		self.partial_data = self.data_fiscal(
			complete_name=self.complete_name, last_name=self.last_name,
			mother_last_name=self.mother_last_name, birth_date=self.birth_date)

	def genera(self):
		curp = self.partial_data
		# Agregar gender de la persona
		curp += self.gender
		# Agregar clave de la entidad
		clave_estado = self.entidad_federativa(self.city)
		curp += clave_estado
		# Agrgar consonantes
		con_paterno = self.consonante_curp(self.last_name)
		curp += con_paterno
		con_materno = self.consonante_curp(self.mother_last_name)
		curp += con_materno
		con_nombres = self.consonante_curp(self.complete_name)
		curp += con_nombres
		# Agregar año al curp
		anio = self.get_year(self.birth_date)
		homoclave = self.homoclave_curp(anio)
		# Agregar homoclave 
		curp += homoclave
		# Agrgar digito verificador
		digito = self.digito_verificador(curp)
		curp += digito
		return curp
	
	def homoclave_curp(self, anio):
		homoclave = ""
		if anio < 2000:
			homoclave = "0"
		elif anio >= 2000:
			homoclave = "A"

		return homoclave

	def digito_verificador(self, curp):
		contador = 18
		count = 0
		valor = 0
		sumaria = 0

		verificadores = {
			'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
			'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18,
			'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'Ñ':24, 'O':25, 'P':26, 'Q':27,
			'R':28, 'S':29, 'T':30, 'U':31, 'V':32, 'W':33, 'X':34, 'Y':35, 'Z':36
		}

		for count in range(0,len(curp)):
			posicion = curp[count]

			for key,value in verificadores.items():
				if posicion == key:
					valor = (value * contador)

			contador = contador - 1
			sumaria = sumaria + valor

		# Sacar el residuo	
		num_ver = sumaria % 10
		# Devuelve el valor absoluto en caso de que sea negativo
		num_ver = abs(10 - num_ver)
		# En caso de que sea 10 el digito es 0
		if num_ver == 10:
			num_ver = 0
		return str(num_ver)	

	@property
	def data(self):
		return self.genera()


class CalculeGeneric(object): 
	_data = {}

	def __init__(self, **kwargs):
		self._datos = kwargs

	@property
	def data(self):
		for cls in self.generadores:		
			data = cls.DATA_REQUIRED

			kargs = {key: self._datos[key] for key in data}
			gen = cls(**kargs)
			gen.genera()
			self._data[gen.key_value] = gen.data

		return self._data