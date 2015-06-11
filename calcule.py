from base import BaseGenerator


class CalculeRFC(BaseGenerator):

	_nombres = None 
	_paterno = None
	_materno = None
	_fecha = None 
	_nombrecompleto = None

	def genera_rfc(self):
		self._rfc = self._origen
		self._nombrecompleto = "%s %s %s" % (self._paterno, self._materno, self._nombres)
		# Cálcula y agrega homoclave al RFC
		self._homoclave = self.homoclave_rfc(self._rfc, self._nombrecompleto)
		self._rfc += self._homoclave
		# Cálcula y agrega digito verificador al RFC
		self._digito = self.numero_verificador(self._rfc)
		self._rfc += self._digito

		return self._rfc

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

	_nombres = None 
	_paterno = None
	_materno = None
	_fecha = None 
	_genero = None
	_estado = None 
	
	def genera_curp(self):
		self._curp = self._origen

		self._curp += self._genero

		clave_estado = self.entidad_federativa(self._estado)
		self._curp += clave_estado

		con_paterno = self.consonante(self._paterno)
		self._curp += con_paterno

		con_materno = self.consonante(self._materno)
		self._curp += con_materno

		con_nombres = self.consonante(self._nombres)
		self._curp += con_nombres

		anio = self.anio_fecha(self._fecha)
		homoclave = self.homoclave_curp(anio)

		self._curp += homoclave

		digito = self.digito_verificador(self._curp)
		self._curp += digito

		return self._curp
	
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

		for count in range(0,len(curp)):
			posicion = curp[count]

			if posicion == "0":
				valor = (0 * contador)
			if posicion == "1":
				valor = (1 * contador)
			if posicion == "2":
				valor = (2 * contador)
			if posicion == "3":
				valor = (3 * contador)
			if posicion == "4":
				valor = (4 * contador)
			if posicion == "5":
				valor = (5 * contador)
			if posicion == "6":
				valor = (6 * contador)
			if posicion == "7":
				valor = (7 * contador)
			if posicion == "8":
				valor = (8 * contador)
			if posicion == "9":
				valor = (9 * contador)
			if posicion == "A":
				valor = (10 * contador)
			if posicion == "B":
				valor = (11 * contador)
			if posicion == "C":
				valor = (12 * contador)
			if posicion == "D":
				valor = (13 * contador)
			if posicion == "E":
				valor = (14 * contador)
			if posicion == "F":
				valor = (15 * contador)
			if posicion == "G":
				valor = (16 * contador)
			if posicion == "H":
				valor = (17 * contador)
			if posicion == "I":
				valor = (18 * contador)
			if posicion == "J":
				valor = (19 * contador)
			if posicion == "K":
				valor = (20 * contador)
			if posicion == "L":
				valor = (21 * contador)
			if posicion == "M":
				valor = (22 * contador)
			if posicion == "N":
				valor = (23 * contador)
			if posicion == "Ñ":
				valor = (24 * contador)
			if posicion == "O":
				valor = (25 * contador)
			if posicion == "P":
				valor = (26 * contador)
			if posicion == "Q":
				valor = (27 * contador)
			if posicion == "R":
				valor = (28 * contador)
			if posicion == "S":
				valor = (29 * contador)
			if posicion == "T":
				valor = (30 * contador)
			if posicion == "U":
				valor = (31 * contador)
			if posicion == "V":
				valor = (32 * contador)
			if posicion == "W":
				valor = (33 * contador)
			if posicion == "X":
				valor = (34 * contador)
			if posicion == "Y":
				valor = (35 * contador)
			if posicion == "Z":
				valor = (36 * contador)

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
	def curp(self):
		return self._curp


class CalculeGeneric(BaseGenerator): 

	def __init__(self):

		super(CalculeGeneric, self).__init__()

		self.genera_curp()
		self.genera_rfc()

	@property
	def data(self):

		value = super(CalculeGeneric, self).data
		return value