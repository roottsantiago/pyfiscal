import datetime
from utils import Utils

class BaseGenerator(object):
	
	_nombres = None 
	_paterno = None
	_materno = None
	_fecha = None 
	_genero = None
	_estado = None 
	_origen = None
	_curp = None
	_rfc = None
	_data = []

	def __init__(self):
		self._nombres = self.nombres
		self._paterno = self.paterno
		self._materno = self.materno
		self._fecha = self.fecha 
		self._genero = self.genero
		self._estado = self.estado

		self.parse_params()
		self.generico()

	def parse_params(self):

		self._nombres = Utils().upper(self._nombres)
		self._paterno = Utils().upper(self._paterno)
		self._materno = Utils().upper(self._materno)
		self._estado = Utils().upper(self._estado)

		self._nombres = Utils().quita_nombre(self._nombres)
		self._paterno = Utils().quita_articulo(self._paterno)
		self._materno = Utils().quita_articulo(self._materno)
		
		self._nombres = Utils().quita_CH_LL(self._nombres)
		self._paterno = Utils().quita_CH_LL(self._paterno)
		self._materno = Utils().quita_CH_LL(self._materno)

	def generico(self):
		# Regresa iniciales del nombre y verifica palabras 
		self._origen = self.iniciales_nombre(self._nombres, self._paterno, self._materno)
		self._origen = self.verifica_palabra(self._origen)
		# Agrega fecha de nacimineto
		fecha_nacimiento = self.parse_fecha(self._fecha)
		self._origen += fecha_nacimiento

		return self._origen
		
	def genera_curp(self):
		self._curp = self._origen

		self._curp += self._genero

		clave_estado = self.entidad_federativa(self._estado)
		self._curp += clave_estado

		con_paterno = Utils().consonante(self._paterno)
		self._curp += con_paterno

		con_materno = Utils().consonante(self._materno)
		self._curp += con_materno

		con_nombres = Utils().consonante(self._nombres)
		self._curp += con_nombres

		anio = Utils().anio_fecha(self._fecha)
		homoclave = self.homoclave_curp(anio)
		self._curp += homoclave

		digito = self.digito_verificador(self._curp)
		self._curp += digito

		return self._curp

	def iniciales_nombre(self, nombres, paterno, materno):

		# No tiene apellido paterno
		if paterno == "" and materno != "":
			iniciales = "XX"
			iniciales += materno[0:2]

		# No tiene apellido materno 
		if materno == "" and paterno != "":
			iniciales = paterno[0:1]
			z1 = len(paterno) - 1
			paterno = paterno[1:z1]

			#Buscamos y agregamos al curp la primera vocal del apellido
			for item in paterno:
				if Utils.esVocal(item):
					iniciales += item
					break

			iniciales += "X"
			iniciales += nombres[0:1]

		if paterno != "" and materno != "":
			iniciales = paterno[0:1]
			z1 = len(paterno) - 1
			paterno = paterno[1:z1]

			for item in paterno:
				if Utils.esVocal(item):
					iniciales += item
					break

			iniciales += materno[0:1]
			iniciales += nombres[0:1]

		return iniciales

	def verifica_palabra(self, rfc):

		palabras = [ 
			"BUEI", "BUEY", "CACA", "CACO", "CAGA", "CAGO", "CAKA", "CAKO", "COGE",
			"COGI", "COJA", "COJE", "COJI", "COJO", "COLA", "CULO", "FALO", "FETO",
			"GETA", "GUEI", "GUEY", "JETA", "JOTO", "KACA", "KACO", "KAGA", "KAGO", 
			"KAKA", "KAKO", "KOGE", "KOGI", "KOJA", "KOJE", "KOJI", "KOJO", "KOLA", 
			"KULO", "LILO", "LOCA", "LOCO", "LOKA", "LOKO", "MAME", "MAMO", "MEAR", 
			"MEAS", "MEON", "MIAR", "MION", "MOCO", "MOKO", "MULA", "MULO", "NACA", 
			"NACO", "PEDA", "PEDO", "PENE", "PIPI", "PITO", "POPO", "PUTA", "PUTO", 
			"QULO", "RATA", "ROBA", "ROBE", "ROBO", "RUIN", "SENO", "TETA", "VUEI", 
			"VUEY", "WUEI", "WUEY",
		]

		for palabra in palabras:
			if palabra == rfc:
				rfc = "XXXX"
				break

		return rfc

	def parse_fecha(self, fecha):
		fecha_nac = ""
		fecha = datetime.datetime.strptime(fecha, '%d-%m-%Y').date()
		anio = str(fecha.year)
		anio = anio[2:4]
		# Rellena con ceros a la izquierda
		mes = str(fecha.month).zfill(2)
		dia = str(fecha.day).zfill(2)

		fecha_nac += anio+mes+dia 

		return fecha_nac


	def entidad_federativa(self, param):
		estado = None	
		estados = { 
			"":"", "AGUASCALIENTES":"AS",
			"BAJA CALIFORNIA":"BC",
			"BAJA CALIFORNIA SUR":"BS",
			"CAMPECHE":"CC",
			"CHIAPAS":"CS",
			"CHIHUAHUA":"CH",
			"COAHUILA":"CL",
			"COLIMA":"CM",
			"DISTRITO FEDERAL":"DF",
			"DURANGO":"DG",
			"GUANAJUATO":"GT",
			"GUERRERO":"GR",
			"HIDALGO":"HG",
			"JALISCO":"JC",
			"MEXICO":"MC",
			"MICHOACAN":"MN",
			"MORELOS":"MS",
			"NAYARIT":"NT",
			"NUEVO LEON":"NL",
			"OAXACA":"OC",
			"PUEBLA":"PL",
			"QUERETARO":"QT",
			"QUINTANA ROO":"QR",
			"SAN LUIS POTOSI":"SP",
			"SINALOA":"SL",
			"SONORA":"SR",
			"TABASCO":"TC",
			"TAMAULIPAS":"TS",
			"TLAXCALA":"TL",
			"VERACRUZ":"VZ",
			"YUCATÁN":"YN",
			"ZACATECAS":"ZS",
			"NACIDO EXTRANJERO":"NE",
		}

		for key, value in estados.items():
			if key == param:
				estado = value
		
		return estado

	def digito_verificador(self, curp):
		contador = 18
		count = 0
		valor = 0
		sumaria = 0

		for count in range(0,len(curp)):
			pstCom = curp[count]

			if pstCom == "0":
				valor = (0 * contador)
			if pstCom == "1":
				valor = (1 * contador)
			if pstCom == "2":
				valor = (2 * contador)
			if pstCom == "3":
				valor = (3 * contador)
			if pstCom == "4":
				valor = (4 * contador)
			if pstCom == "5":
				valor = (5 * contador)
			if pstCom == "6":
				valor = (6 * contador)
			if pstCom == "7":
				valor = (7 * contador)
			if pstCom == "8":
				valor = (8 * contador)
			if pstCom == "9":
				valor = (9 * contador)
			if pstCom == "A":
				valor = (10 * contador)
			if pstCom == "B":
				valor = (11 * contador)
			if pstCom == "C":
				valor = (12 * contador)
			if pstCom == "D":
				valor = (13 * contador)
			if pstCom == "E":
				valor = (14 * contador)
			if pstCom == "F":
				valor = (15 * contador)
			if pstCom == "G":
				valor = (16 * contador)
			if pstCom == "H":
				valor = (17 * contador)
			if pstCom == "I":
				valor = (18 * contador)
			if pstCom == "J":
				valor = (19 * contador)
			if pstCom == "K":
				valor = (20 * contador)
			if pstCom == "L":
				valor = (21 * contador)
			if pstCom == "M":
				valor = (22 * contador)
			if pstCom == "N":
				valor = (23 * contador)
			if pstCom == "Ñ":
				valor = (24 * contador)
			if pstCom == "O":
				valor = (25 * contador)
			if pstCom == "P":
				valor = (26 * contador)
			if pstCom == "Q":
				valor = (27 * contador)
			if pstCom == "R":
				valor = (28 * contador)
			if pstCom == "S":
				valor = (29 * contador)
			if pstCom == "T":
				valor = (30 * contador)
			if pstCom == "U":
				valor = (31 * contador)
			if pstCom == "V":
				valor = (32 * contador)
			if pstCom == "W":
				valor = (33 * contador)
			if pstCom == "X":
				valor = (34 * contador)
			if pstCom == "Y":
				valor = (35 * contador)
			if pstCom == "Z":
				valor = (36 * contador)

			contador = contador - 1
			sumaria = sumaria + valor
			
		# Sacar el residuo	
		num_ver = sumaria % 10
		# Devuelve el valor absoluto en caso de que sea negativo
		num_ver = abs(10 - num_ver)
		#En caso de que sea 10 el digito es 0
		if num_ver == 10:
			num_ver = 0

		return str(num_ver)	

	def homoclave_curp(self, anio):
		homoclave = ""

		if anio < 2000:
			homoclave = "0"
		elif anio >= 2000:
			homoclave = "A"

		return homoclave

	@property
	def data(self):
		self._data.append(self._curp)
		self._data.append(self._rfc)
		return self._data