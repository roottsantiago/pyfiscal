from base import BaseGenerator


class CalculeRFC(BaseGenerator):

	_nombrecompleto = None

	def genera_rfc(self):
		self._rfc = self._origen
		self._nombrecompleto = "%s %s %s" % (self._paterno, self._materno, self._nombres)
		# Cálcula y agrega homoclave al RFC
		self._homoclave = self.homoclave(self._rfc, self._nombrecompleto)
		self._rfc += self._homoclave
		# Cálcula y agrega digito verificador al RFC
		self._digito = self.numero_verificador(self._rfc)
		self._rfc += self._digito

		return self._rfc

	def homoclave(self, rfc, nombrecompleto):
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
		for count in range(0,len(nombrecompleto)):
			letra = nombrecompleto[count] 
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
		else :
			return a


	@property
	def rfc(self):
		return self._rfc


class CalculeCURP(BaseGenerator):

	@property
	def curp(self):
		curp = super(CalculeCURP, self).curp
		return curp

class CalculeGeneric(BaseGenerator): 

	def __init__(self):

		super(CalculeGeneric, self).__init__()

		self.genera_curp()
		self.genera_rfc()

	@property
	def data(self):

		value = super(CalculeGeneric, self).data
		return value