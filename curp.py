
import datetime
class curp:
	nombre = "Tomas" 
	apellidoPaterno = "Santiago" 
	apellidoMatermo = "Gonzalez"
	fechaNacimiento = "1989-11-16"
	sexo = "M"
	estadoNacimiento = "Hidalgo"

	fNac = datetime.datetime.strptime(fechaNacimiento, '%Y-%m-%d').date()
	#print(fNac)

	def calculaCurp(self):  
		print("Hola")

cp = curp()
cp.calculaCurp()   