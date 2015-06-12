from calcule import CalculeRFC, CalculeCURP, CalculeGeneric

class GenerateDataFiscal(CalculeGeneric):
	generadores = (CalculeCURP, CalculeRFC)


datos = {
	'fecha': '16-11-1989',
	'nombres': 'Tomas',
	'paterno': 'Santiago',
	'materno': 'Gonzalez',
	'genero': 'H',
	'estado': 'HIDALGO',
}

todo = GenerateDataFiscal(**datos).data
print(todo)