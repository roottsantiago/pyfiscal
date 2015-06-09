from calcule import Calcule


class GenerateRFC(Calcule):
	
	nombres = "tomas"
	apellido_paterno = "santiago"
	apellido_materno = "gonzalez"
	fecha_nacimiento = "16-11-1989"
	genero = "H"
	lugar_nacimiento = ""

class GenerateCURP(Calcule):

	nombres = "tomas"
	apellido_paterno = "santiago"
	apellido_materno = "gonzalez"
	fecha_nacimiento = "16-11-1989"
	genero = "H"
	lugar_nacimiento = "hidalgo"


curp = GenerateCURP().CURP()
rfc = GenerateRFC().RFC()

print(curp)
print(rfc)
