from calcule import CalculeRFC, CalculeCURP, CalculeGeneric


class GenerateDataFiscal(CalculeRFC, CalculeCURP, CalculeGeneric):
	nombres = "tomas"
	paterno = "santiago"
	materno = "gonzalez"
	fecha = "16-11-1989"
	genero = "H"
	estado = "hidalgo"


datos = GenerateDataFiscal().data
print(datos)