
import datetime
from utils import *
class curp:
	fechaNacimiento = "1989-11-16"

	fNac = datetime.datetime.strptime(fechaNacimiento, '%Y-%m-%d').date()
	#print(fNac)

	def calculaCurp(self):  
		test = 'prueba'

	def general(self):
		nom = "Tomas"
		apa = "Santiago"
		ama = "Gonzalez"
		rfc = ""

		nombre = nom.upper()
		pellidoPa = apa.upper()
		pellidoMa = ama.upper()

		nombre = nombre.strip()
		pellidoPa = pellidoPa.strip()
		pellidoMa = pellidoMa.strip()

		pellidoPa = utils.quitaArticulo(pellidoPa)
		pellidoMa = utils.quitaArticulo(pellidoMa)
		nombre = utils.quitaNombre(nombre)

		print(pellidoPa)
		print(pellidoMa)
		print(nombre)

cp = curp()
cp.calculaCurp()
cp.general()   