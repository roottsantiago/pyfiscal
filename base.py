import datetime
from utils import Utils

class BaseGenerator(object):

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
				if Utils().vocal(item):
					iniciales += item
					break

			iniciales += "X"
			iniciales += nombres[0:1]

		if paterno != "" and materno != "":
			iniciales = paterno[0:1]
			z1 = len(paterno)-1
			paterno = paterno[1:z1]

			for item in paterno:
				if Utils().vocal(item):
					iniciales += item
					break

			iniciales += materno[0:1]
			iniciales += nombres[0:1]

		return iniciales

	def verifica_palabra(self, rfc):

		palabras = [ 
			'BUEI', 'BUEY', 'CACA', 'CACO', 'CAGA', 'CAGO', 'CAKA', 'CAKO', 'COGE',
			'COGI', 'COJA', 'COJE', 'COJI', 'COJO', 'COLA', 'CULO', 'FALO', 'FETO',
			'GETA', 'GUEI', 'GUEY', 'JETA', 'JOTO', 'KACA', 'KACO', 'KAGA', 'KAGO', 
			'KAKA', 'KAKO', 'KOGE', 'KOGI', 'KOJA', 'KOJE', 'KOJI', 'KOJO', 'KOLA', 
			'KULO', 'LILO', 'LOCA', 'LOCO', 'LOKA', 'LOKO', 'MAME', 'MAMO', 'MEAR', 
			'MEAS', 'MEON', 'MIAR', 'MION', 'MOCO', 'MOKO', 'MULA', 'MULO', 'NACA', 
			'NACO', 'PEDA', 'PEDO', 'PENE', 'PIPI', 'PITO', 'POPO', 'PUTA', 'PUTO', 
			'QULO', 'RATA', 'ROBA', 'ROBE', 'ROBO', 'RUIN', 'SENO', 'TETA', 'VUEI', 
			'VUEY', 'WUEI', 'WUEY',
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
			'':'', 'AGUASCALIENTES':'AS', 'BAJA CALIFORNIA':'BC',
			'BAJA CALIFORNIA SUR':'BS', 'CAMPECHE':'CC', 'CHIAPAS':'CS',
			'CHIHUAHUA':'CH', 'COAHUILA':'CL', 'COLIMA':'CM', 'DISTRITO FEDERAL':'DF',
			'DURANGO':'DG', 'GUANAJUATO':'GT', 'GUERRERO':'GR', 'HIDALGO':'HG',
			'JALISCO':'JC', 'MEXICO':'MC', 'MICHOACAN':'MN', 'MORELOS':'MS',
			'NAYARIT':'NT', 'NUEVO LEON':'NL', 'OAXACA':'OC', 'PUEBLA':'PL',
			'QUERETARO':'QT', 'QUINTANA ROO':'QR', 'SAN LUIS POTOSI':'SP',
			'SINALOA':'SL', 'SONORA':'SR', 'TABASCO':'TC', 'TAMAULIPAS':'TS',
			'TLAXCALA':'TL', 'VERACRUZ':'VZ', 'YUCATÁN':'YN', 'ZACATECAS':'ZS',
			'NACIDO EXTRANJERO':'NE',
		}

		for key, value in estados.items():
			if key == param:
				estado = value
		
		return estado

	def consonante(self, param):
		consonante = "X"
		consonante = Utils().consonate_curp(param)
		return consonante

	def anio_fecha(self, fecha):
		anio = Utils().anio(fecha)
		return anio

	@property
	def data(self):
		self._data.append(self._curp)
		self._data.append(self._rfc)
		return self._data