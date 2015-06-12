import datetime
from utils import Utils

class BaseGenerator(object):

	def genera(self):
		raise NotImplementedError("No implemetado.")

	def parse(self, nombres, paterno, materno='', estado=None):
		
		if estado != None:
			self.estado = Utils().upper(estado)

		self.nombres = Utils().upper(nombres)
		self.paterno = Utils().upper(paterno)
		self.materno = Utils().upper(materno)
		
		self.nombres = Utils().quita_nombre(self.nombres)
		self.paterno = Utils().quita_articulo(self.paterno)
		self.materno = Utils().quita_articulo(self.materno)
		
		self.nombres = Utils().quita_CH_LL(self.nombres)
		self.paterno = Utils().quita_CH_LL(self.paterno)
		self.materno = Utils().quita_CH_LL(self.materno)

	def base_dato_fiscal(self, nombres, paterno, materno, fecha):
		# Regresa iniciales del nombre y verifica palabras 
		dato_fiscal = self.iniciales_nombre(nombres, paterno, materno)
		dato_fiscal = self.verifica_palabra(dato_fiscal)
		# Agrega fecha de nacimineto
		fecha_nacimiento = self.parse_fecha(fecha)
		dato_fiscal += fecha_nacimiento

		return dato_fiscal
		
	def iniciales_nombre(self, nombres, paterno, materno):
		iniciales = ''

		# No tiene apellido paterno
		if paterno == None:
			
			iniciales += "XX"
			iniciales += materno[0:1]
			iniciales += nombres[0:1]

		# No tiene apellido materno 
		if materno =='':

			iniciales = paterno[0:1]

			size = len(paterno)-1
			paterno = paterno[1:size]
			#Buscamos la primera vocal del apellido
			for item in paterno:
				if Utils().vocal(item):
					vocal = item
					break

			iniciales += vocal
			iniciales += 'X'
			iniciales += nombres[0:1]

		if paterno != None and materno != None:
			iniciales = paterno[0:1]
			
			size = len(paterno)-1
			paterno = paterno[1:size]

			for item in paterno:
				if Utils().vocal(item):
					vocal = item
					break

			# Iniciales	
			iniciales += vocal 
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
