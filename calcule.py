# -*- coding: utf-8 -*-
from base import BaseGenerator

import unicodedata


class CalculeRFC(BaseGenerator):
	
	key_value = 'rfc'
	DATOS_REQUERIDOS = ( 'nombres','paterno', 'materno','fecha')
	_dato_parcial = None

	def __init__(self, **kargs):

		self.nombres = kargs['nombres']
		self.paterno = kargs['paterno']
		self.materno = kargs['materno']
		self.fecha = kargs['fecha']

		self.parse(
			nombres=self.nombres, paterno=self.paterno, materno=self.materno
		)
		
		self._dato_parcial = self.base_dato_fiscal(
			nombres=self.nombres, paterno=self.paterno, materno=self.materno,
			fecha=self.fecha
		)

	def genera(self):
		if self.materno is not None:
			nombrecompleto = u"%s %s %s" % (self.paterno, self.materno, self.nombres)
		else:
			nombrecompleto = u"%s %s" % (self.paterno, self.nombres)


		# Cálcula y agrega homoclave al RFC
		rfc = self._dato_parcial
		homoclave = self.homoclave_rfc(self._dato_parcial, nombrecompleto)
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

	key_value = 'curp'
	DATOS_REQUERIDOS = ('nombres','paterno', 'materno','fecha', 'genero', 'estado')
	_dato_parcial = None

	def __init__(self, **kargs):

		self.nombres = kargs['nombres']
		self.paterno = kargs['paterno']
		self.materno = kargs['materno']
		self.fecha = kargs['fecha']
		self.genero = kargs['genero']
		self.estado = kargs['estado']

		self.parse(
			nombres=self.nombres, paterno=self.paterno, materno=self.materno,
			estado=self.estado
		)
		
		self._dato_parcial = self.base_dato_fiscal(
			nombres=self.nombres, paterno=self.paterno, materno=self.materno,
			fecha=self.fecha
		)

	def genera(self):
		curp = self._dato_parcial
		# Agregar genero de la persona
		curp += self.genero
		# Agregar clave de la entidad
		clave_estado = self.entidad_federativa(self.estado)
		curp += clave_estado
		# Agrgar consonantes
		con_paterno = self.consonante_curp(self.paterno)
		curp += con_paterno
		con_materno = self.consonante_curp(self.materno)
		curp += con_materno
		con_nombres = self.consonante_curp(self.nombres)
		curp += con_nombres
		# Agregar año al curp
		anio = self.anio_fecha(self.fecha)
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
	def __init__(self, **_datos):
		self._datos =_datos

	@property
	def data(self):
		for cls in self.generadores:
			
			
			requeridos = cls.DATOS_REQUERIDOS

			kargs = {key: self._datos[key] for key in requeridos}
			gen = cls(**kargs)
			gen.genera()
			self._data[gen.key_value] = gen.data

		return self._data