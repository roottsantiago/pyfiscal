from calcule import Calcule


class Generate(Calcule):
	nombres = "tomas"
	paterno = "santiago"
	materno = "gonzalez"
	fecha = "16-11-1989"
	genero = "H"
	estado = "hidalgo"
	x = 9000

datos = Generate().data
print(datos)