from utils import *
from stringBuilder import*

class general:

	def datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento, origen):
		generico = ""

		# Cambiamos todo a mayúsculas
		nombre = nombre.upper()
		apellidoPaterno = ape_paterno.upper()
		apellidoMaterno = ape_materno.upper()

		# Quitamos los espacios al principio y final del nombre y apellidos
		nombre = nombre.strip()
		apellidoPaterno = apellidoPaterno.strip()
		apellidoMaterno = apellidoMaterno.strip()

		# Quitamos los artículos de los apellidos
		apellidoPaterno = utils.quitaArticulo(apellidoPaterno)
		apellidoMaterno = utils.quitaArticulo(apellidoMaterno)

		# Quitamos nombres Jose y Maria
		nombre = utils.quitaNombre(nombre)

		# Quita la CH y la LL
		apellidoPaterno = utils.quitarCHLL(apellidoPaterno)
		apellidoMaterno = utils.quitarCHLL(apellidoMaterno)
		nombre = utils.quitarCHLL(nombre)
		
		origen_curp = 'CURP'
		if origen_curp == origen:
			generico = utils.calculaOrigenCurp(nombre, apellidoPaterno, apellidoMaterno)

		# Verificar los datos que no tenga palabras obsenas 
		generico = utils.verificarPalabras(generico, origen)

		# Agregamos la fecha de Nacimiento
		generico = utils.fechaNacimiento(generico, fecha_nacimiento)
		return generico

	def calculaHomoclaveRFC(rfc, nombre_completo, fecha_nac):

		dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

		nombre_numero = StringBuilder()
		#Agregamos un cero al inicio de la representación númerica del nombre
        nombre_numero.Append("0")

		valorSuma = 0 
		
		lst_table1 = []
		lst_table2 = []
		lst_table3 = []

		lst_table1.append({" ":0})
		lst_table1.append({"&":10})
		lst_table1.append({"A":11})
		lst_table1.append({"B":12})
		lst_table1.append({"C":13})
		lst_table1.append({"D":14})
		lst_table1.append({"E":15})
		lst_table1.append({"F":16})
		lst_table1.append({"G":17})
		lst_table1.append({"H":18})
		lst_table1.append({"I":19})
		lst_table1.append({"J":21})
		lst_table1.append({"K":22})
		lst_table1.append({"L":23})
		lst_table1.append({"M":24})
		lst_table1.append({"N":25})
		lst_table1.append({"O":26})
		lst_table1.append({"P":27})
		lst_table1.append({"Q":28})
		lst_table1.append({"R":29})
		lst_table1.append({"S":32})
		lst_table1.append({"T":33})
		lst_table1.append({"U":34})
		lst_table1.append({"V":35})
		lst_table1.append({"W":36})
		lst_table1.append({"X":37})
		lst_table1.append({"Y":38})
		lst_table1.append({"Z":39})
		lst_table1.append({"Ñ":40})
		lst_table1.append({"0":0})
		lst_table1.append({"1":1})
		lst_table1.append({"2":2})
		lst_table1.append({"3":3})
		lst_table1.append({"4":4})
		lst_table1.append({"5":5})
		lst_table1.append({"6":6})
		lst_table1.append({"7":7})
		lst_table1.append({"8":8})
		lst_table1.append({"9":9})
		# Empieza tabla2
		lst_table2.append({0:"1"})
		lst_table2.append({1:"2"})
		lst_table2.append({2:"3"})
		lst_table2.append({3:"4"})
		lst_table2.append({4:"5"})
		lst_table2.append({5:"6"})
		lst_table2.append({6:"7"})
		lst_table2.append({7:"8"})
		lst_table2.append({8:"9"})
		lst_table2.append({9:"A"})
		lst_table2.append({10:"B"})
		lst_table2.append({11:"C"})
		lst_table2.append({12:"D"})
		lst_table2.append({13:"E"})
		lst_table2.append({14:"F"})
		lst_table2.append({15:"G"})
		lst_table2.append({16:"H"})
		lst_table2.append({17:"I"})
		lst_table2.append({18:"J"})
		lst_table2.append({19:"K"})
		lst_table2.append({20:"L"})
		lst_table2.append({21:"M"})
		lst_table2.append({22:"N"})
		lst_table2.append({23:"P"})
		lst_table2.append({24:"Q"})
		lst_table2.append({25:"R"})
		lst_table2.append({26:"S"})
		lst_table2.append({27:"T"})
		lst_table2.append({28:"U"})
		lst_table2.append({29:"V"})
		lst_table2.append({30:"W"})
		lst_table2.append({31:"X"})
		lst_table2.append({32:"Y"})
		lst_table2.append({33:"Z"})
		# Empieza tabla3
		lst_table3.append({"A":10})
		lst_table3.append({"B":11})
		lst_table3.append({"C":12})
		lst_table3.append({"D":13})
		lst_table3.append({"E":14})
		lst_table3.append({"F":15})
		lst_table3.append({"G":16})
		lst_table3.append({"H":17})
		lst_table3.append({"I":18})
		lst_table3.append({"J":19})
		lst_table3.append({"K":20})
		lst_table3.append({"L":21})
		lst_table3.append({"M":22})
		lst_table3.append({"N":23})
		lst_table3.append({"&":24})
		lst_table3.append({"O":25})
		lst_table3.append({"P":26})
		lst_table3.append({"Q":27})
		lst_table3.append({"R":28})
		lst_table3.append({"S":29})
		lst_table3.append({"T":30})
		lst_table3.append({"U":31})
		lst_table3.append({"V":32})
		lst_table3.append({"W":33})
		lst_table3.append({"X":34})
		lst_table3.append({"Y":35})
		lst_table3.append({"Z":36})
		lst_table3.append({" ":37})
		lst_table3.append({"Ñ":38})
		lst_table3.append({"0":0})
		lst_table3.append({"1":1})
		lst_table3.append({"2":2})
		lst_table3.append({"3":3})
		lst_table3.append({"4":4})
		lst_table3.append({"5":5})
		lst_table3.append({"6":6})
		lst_table3.append({"7":7})
		lst_table3.append({"8":8})
		lst_table3.append({"9":9})

		

		print(lst_table1)
		print(lst_table2)
		print(lst_table3)