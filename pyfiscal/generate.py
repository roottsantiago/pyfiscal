# -*- coding: utf-8 -*-
import unicodedata
from .base import BaseGenerator


class GenerateRFC(BaseGenerator):
	key_value = 'rfc'
	DATA_REQUIRED = ('complete_name', 'last_name', 'mother_last_name', 'birth_date')
	partial_data = None

	def __init__(self, **kwargs):
		self.complete_name = kwargs.get('complete_name')
		self.last_name = kwargs.get('last_name')
		self.mother_last_name = kwargs.get('mother_last_name')
		self.birth_date = kwargs.get('birth_date')

		self.parse(
			complete_name=self.complete_name, 
			last_name=self.last_name, 
			mother_last_name=self.mother_last_name
		)
	
		self.partial_data = self.data_fiscal(
			complete_name=self.complete_name,
			last_name=self.last_name, 
			mother_last_name=self.mother_last_name, 
			birth_date=self.birth_date
		)

	def calculate(self):
		full_name = self.full_name
		rfc = self.partial_data

		hc = self.homoclave(self.partial_data, full_name)
		rfc += '%s' % hc
		rfc += self.verification_number(rfc)
		return rfc

	def homoclave(self, rfc, complete_name):
		nombre_numero = '0'
		summary = 0 
		div = 0 
		mod = 0

		rfc1 = {
			' ':00, '&':10, 'Ñ':10, 'A':11, 'B':12, 'C':13, 'D':14, 'E':15, 'F':16,
			'G':17, 'H':18, 'I':19, 'J':21, 'K':22, 'L':23, 'M':24, 'N':25, 'O':26,
			'P':27, 'Q':28, 'R':29, 'S':32, 'T':33, 'U':34, 'V':35, 'W':36, 'X':37,
			'Y':38, 'Z':39, '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
			'8':8,'9':9,
		}
		rfc2 = {
			0:'1', 1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8', 8:'9', 9:'A', 10:'B',
			11:'C', 12:'D', 13:'E', 14:'F', 15:'G', 16:'H', 17:'I', 18:'J', 19:'K',
			20:'L', 21:'M', 22:'N', 23:'P', 24:'Q', 25:'R', 26:'S', 27:'T', 28:'U',
			29:'V', 30:'W', 31:'X', 32:'Y',
		}

		# Recorrer el nombre y convertir las letras en su valor numérico.
		for count in range(0, len(complete_name)):
			letra = self.remove_accents(complete_name[count])

			nombre_numero += self.rfc_set(str(rfc1[letra]),'00')
		# La formula es:
			# El caracter actual multiplicado por diez mas el valor del caracter
			# siguiente y lo anterior multiplicado por el valor del caracter siguiente.
		for count in range(0,len(nombre_numero)-1):
			count2 = count+1
			summary += ((int(nombre_numero[count])*10) + int(nombre_numero[count2])) * int(nombre_numero[count2])
		
		div = summary % 1000
		mod = div % 34
		div = (div-mod)/34
		homoclave = ''
		homoclave += self.rfc_set(rfc2[int(div)], 'Z')
		homoclave += self.rfc_set(rfc2[int(mod)], 'Z')
		return homoclave

	def verification_number(self, rfc):
		"""
		Anexo 3 - Tabla de valores para la generación del código verificador
		del registro federal de contribuyentes. 
		"""
		suma_numero = 0 
		suma_parcial = 0
		digito = None 

		rfc3 = (
			('0', 0), ('D', 13), ('P', 26),
			('1', 1), ('E', 14), ('Q', 27),
			('2', 2), ('F', 15), ('R', 28),
			('3', 3), ('G', 16), ('S', 29),
			('4', 4), ('H', 17), ('T', 30),
			('5', 5), ('I', 18), ('U', 31),
			('6', 6), ('J', 19), ('V', 32),
			('7', 7), ('K', 20), ('W', 33),
			('8', 8), ('L', 21), ('X', 34),
			('9', 9), ('M', 22), ('Y', 35),
			('A', 10), ('N', 23), ('Z', 36),
			('B', 11), ('&', 24), (' ',	37),
			('C', 12), ('O', 25), ('Ñ', 38),
		)

		# rfc3 = {
		# 	'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18,
		# 	'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':25, 'P':26, 'Q':27, 'R':28,
		# 	'S':29, 'T':30, 'U':31, 'V':32, 'W':33, 'X':34, 'Y':35, 'Z':36, '0':0,
		# 	'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '':24,
		# 	' ':37,
		# }


		# 2.- Una vez asignados los valores se aplicará la siguiente forma tomando como base el factor 13
		# en orden descendente a cada letra y número del R.F.C. para su multiplicación,
		# de acuerdo a la siguiente formula: (Vi * (Pi + 1)) + (Vi * (Pi + 1)) + ..............+ (Vi * (Pi + 1)) MOD 11 
		rfc3 = dict((x, y) for x, y in rfc3)
	
		for count in range(0,len(rfc)):
			letra = rfc[count]
	
			if rfc3.get(letra):
				suma_numero = rfc3.get(letra)
				suma_parcial += (suma_numero*(14-(count+1)))

		# 3.- El resultado de la suma se divide entre el factor 11.

		# Si el residuo es igual a cero, este será el valor que se le asignará al dígito verificador.
		# Si el residuo es mayor a cero se restará este al factor 11: 11-3 =8
		# Si el residuo es igual a 10 el dígito verificador será “ A”.
		# Si el residuo es igual a cero el dígito verificador será cero. Por lo tanto “ 8 “
		# es el dígito verificador de este ejemplo: GODE561231GR8.

		residuo = suma_parcial % 11
		
		if residuo == 0:
			digito = '0'
		if residuo == 10:
			digito = 'A'
		if residuo > 0:
			digito = str((11-residuo))
		return  digito

	def rfc_set(self, a, b):
		if a == b:
			return b
		else:
			return a

	@property
	def data(self):
		return self.calculate()


class GenerateCURP(BaseGenerator):
	""" Generate CURP"""
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
		self.state_code = kwargs.get('state_code')
		self.parse(complete_name=self.complete_name, last_name=self.last_name,
				   mother_last_name=self.mother_last_name, city=self.city, state_code=self.state_code)

		self.partial_data = self.data_fiscal(
			complete_name=self.complete_name, last_name=self.last_name,
			mother_last_name=self.mother_last_name, birth_date=self.birth_date)

	def calculate(self):
		curp = self.partial_data
		statecode = self.state_code
		
		if self.city is not None:
			statecode = self.city_search(self.city)
		elif self.state_code is not None:
			statecode = self.state_code
		else: 
			raise AttributeError("No such attribute: state_code")

		lastname = self.get_consonante(self.last_name)
		mslastname = self.get_consonante(self.mother_last_name)
		name = self.get_consonante(self.complete_name)
		year = self.get_year(self.birth_date)
		hc = self.homoclave(year)

		curp += '%s%s%s%s%s%s' % (self.gender, statecode, lastname,
			mslastname, name, hc)
		curp += self.check_digit(curp)
		return curp
	
	def homoclave(self, year):
		hc = ''
		if year < 2000:
			hc = '0'
		elif year >= 2000:
			hc = 'A'
		return hc

	def check_digit(self, curp):
		value = 0
		summary = 0
		checkers = {
			'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
			'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18,
			'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'Ñ':24, 'O':25, 'P':26, 'Q':27,
			'R':28, 'S':29, 'T':30, 'U':31, 'V':32, 'W':33, 'X':34, 'Y':35, 'Z':36
		}

		count = 0
		count2 = 18
		for count in range(0,len(curp)):
			posicion = curp[count]
			for k, v in checkers.items():
				if posicion == k:
					value = (v * count2)
			count2 = count2 - 1
			summary = summary + value
		num_ver = summary % 10 # Residue
		num_ver = abs(10 - num_ver)	#Returns the absolute value in case it is negative.
		if num_ver == 10: 
			num_ver = 0
		return str(num_ver)	

	@property
	def data(self):
		return self.calculate()


class GenerateNSS(BaseGenerator):
	"""
	class for CalculeNSS

	"""
	def __init__(self, nss):
		self.nss = nss

	def is_valid(self):
		validated = len(self.nss)
		if not validated is 11:  # 11 dígitos y subdelegación válida
			return False

		sub_deleg = int(self.nss[0:2])
		year = self.current_year() % 100
		high_date  = int(self.nss[2:4])
		birth_date = int(self.nss[4:6])

		if sub_deleg is not 97:
			if high_date <= year:
				high_date += 100
			if birth_date <= year: 
				birth_date += 100
			if birth_date  >  high_date:
				print('Error: Se dio de alta antes de nacer.')
				return False
		return self._is_luhn_valid()

	def _is_luhn_valid(self): #example 4896889802135
		""" Validate an entry with a check digit. """
		num = list(map(int, str(self.nss)))
		return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

	def _calculate_luhn(self):
		""" Calculation of said digit. """
		num = list(map(int, str(self.nss)))
		check_digit = 10 - sum(num[-2::-2] + [sum(divmod(d * 2, 10)) for d in num[::-2]]) % 10	
		return 0 if check_digit == 10 else check_digit

	@property
	def data(self):
		return self._calculate_luhn()


class GenericGeneration(object): 
	_data = {}

	def __init__(self, **kwargs):
		self._datos = kwargs

	@property
	def data(self):
		for cls in self.generadores:		
			data = cls.DATA_REQUIRED
			kargs = {key: self._datos[key] for key in data}
			gen = cls(**kargs)
			gen.calculate()
			self._data[gen.key_value] = gen.data

		return self._data