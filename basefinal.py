from utils import Utils

class BaseGenerator(object):

	def __init__(self):
		pass

	def forma_rfc(self, nombres, paterno, materno, nacimiento):
		
		nombres = Utils().upper(nombres)
		paterno = Utils().upper(paterno)
		materno = Utils().upper(materno)
		nacimiento = Utils().upper(nacimiento)

		paterno = Utils().quita_articulo(paterno)
		materno = Utils().quita_articulo(materno)

		nombres = Utils().quita_nombre(nombres)
		print(nombres)
