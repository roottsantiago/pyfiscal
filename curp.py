
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
		#RFC que se regresará
		rfc = ""
		#Cambiamos todo a mayúsculas
		nombre = nom.upper()
		pellidoPa = apa.upper()
		pellidoMa = ama.upper()
		#Quitamos los espacios al principio y final del nombre y apellidos
		nombre = nombre.strip()
		pellidoPa = pellidoPa.strip()
		pellidoMa = pellidoMa.strip()
		#Quitamos los artículos de los apellidos
		pellidoPa = utils.quitaArticulo(pellidoPa)
		pellidoMa = utils.quitaArticulo(pellidoMa)
		#Quitamos nombres Jose y Maria
		nombre = utils.quitaNombre(nombre)

		#print(pellidoPa)
		#print(pellidoMa)
		#print(nombre)

		# Obtener consonante apellido paterno
		consonante = "";
		if pellidoPa != "":
			consonante = utils.getConsonate(pellidoPa)
			if consonante != "":
				consonante = "X";
				rfc = rfc + consonante
			else:
				rfc = rfc + "X"


cp = curp()
cp.calculaCurp()
cp.general()   