from calcule import CalculeRFC, CalculeCURP, CalculeGeneric


class GenerateDataFiscal(CalculeRFC, CalculeCURP, CalculeGeneric):
	nombres = "Tomas"
	paterno = "Santiago"
	materno = "Gonzalez"
	fecha = "16-11-1989"
	genero = "H"
	estado = "hidalgo"




rfc = GenerateDataFiscal().rfc
print(rfc)

curp = GenerateDataFiscal().curp
print(curp)

datos = GenerateDataFiscal().data
print(datos)