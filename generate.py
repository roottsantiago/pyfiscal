from calcule import Calcule


class GenerateRFC(Calcule):
	
	nombres = "tomas"
	apellido_paterno = "santiago"
	apellido_materno = "gonzalez"
	fecha_nacimiento = "16-11-1989"
	genero = "H"
	entidad_federativa = ""

class GenerateCURP(Calcule):

	nombres = "tomas"
	apellido_paterno = "santiago"
	apellido_materno = "gonzalez"
	fecha_nacimiento = "16-11-1989"
	genero = "H"
	entidad_federativa = "hidalgo"


curp = GenerateCURP().CURP()
rfc = GenerateRFC().RFC()

print(curp)
print(rfc)
