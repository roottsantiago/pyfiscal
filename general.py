from utils import *
from stringBuilder import*

class General:

	def datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento, origen):
		generico = ""

		# Cambiamos todo a mayúsculas
		nombre = nombre.upper()
		ape_paterno = ape_paterno.upper()
		ape_materno = ape_materno.upper()

		# Quitamos los espacios al principio y final del nombre y apellidos
		nombre = nombre.strip()
		apellidoPaterno = ape_paterno.strip()
		apellidoMaterno = ape_materno.strip()

		# Quitamos los artículos de los apellidos
		apellidoPaterno = Utils.quitaArticulo(apellidoPaterno)
		apellidoMaterno = Utils.quitaArticulo(apellidoMaterno)

		# Quitamos nombres Jose y Maria
		nombre = Utils.quitaNombre(nombre)

		# Quita la CH y la LL
		apellidoPaterno = Utils.quitarCHLL(apellidoPaterno)
		apellidoMaterno = Utils.quitarCHLL(apellidoMaterno)
		nombre = Utils.quitarCHLL(nombre)
		
		
		if origen == "CURP":
			generico = Utils.calculaOrigenCurp(nombre, apellidoPaterno, apellidoMaterno)
		elif origen == "RFC":
			generico = Utils.calculaOrigenRFc(nombre, apellidoPaterno, apellidoMaterno)


		# Verificar los datos que no tenga palabras obsenas 
		generico = Utils.verificarPalabras(generico, origen)

		# Agregamos la fecha de Nacimiento
		generico = Utils.fechaNacimiento(generico, fecha_nacimiento)
		return generico

	def entidadFederativa(param):
		estado = None	
		dic_estados = { 
			"":"",
			"AGUASCALIENTES":"AS",
			"BAJA CALIFORNIA":"BC",
			"BAJA CALIFORNIA SUR":"BS",
			"CAMPECHE":"CC",
			"CHIAPAS":"CS",
			"CHIHUAHUA":"CH",
			"COAHUILA":"CL",
			"COLIMA":"CM",
			"DISTRITO FEDERAL":"DF",
			"DURANGO":"DG",
			"GUANAJUATO":"GT",
			"GUERRERO":"GR",
			"HIDALGO":"HG",
			"JALISCO":"JC",
			"MEXICO":"MC",
			"MICHOACAN":"MN",
			"MORELOS":"MS",
			"NAYARIT":"NT",
			"NUEVO LEON":"NL",
			"OAXACA":"OC",
			"PUEBLA":"PL",
			"QUERETARO":"QT",
			"QUINTANA ROO":"QR",
			"SAN LUIS POTOSI":"SP",
			"SINALOA":"SL",
			"SONORA":"SR",
			"TABASCO":"TC",
			"TAMAULIPAS":"TS",
			"TLAXCALA":"TL",
			"VERACRUZ":"VZ",
			"YUCATÁN":"YN",
			"ZACATECAS":"ZS",
			"NACIDO EXTRANJERO":"NE"
		}
		
		for key, value in dic_estados.items():
			if key == param:
				estado = value
		return estado

	def digitoVerificador(curp, anio):
		contador = 18
		count = 0
		valor = 0
		sumaria = 0
		homoclave = ""

		while (count <= 15):
			pstCom = curp[count:1]

			if pstCom == "0":
				valor = (0 * contador)
			if pstCom == "1":
				valor = (1 * contador)
			if pstCom == "2":
				valor = (2 * contador)
			if pstCom == "3":
				valor = (3 * contador)
			if pstCom == "4":
				valor = (4 * contador)
			if pstCom == "5":
				valor = (5 * contador)
			if pstCom == "6":
				valor = (6 * contador)
			if pstCom == "7":
				valor = (7 * contador)
			if pstCom == "8":
				valor = (8 * contador)
			if pstCom == "9":
				valor = (9 * contador)
			if pstCom == "A":
				valor = (10 * contador)
			if pstCom == "B":
				valor = (11 * contador)
			if pstCom == "C":
				valor = (12 * contador)
			if pstCom == "D":
				valor = (13 * contador)
			if pstCom == "E":
				valor = (14 * contador)
			if pstCom == "F":
				valor = (15 * contador)
			if pstCom == "G":
				valor = (16 * contador)
			if pstCom == "H":
				valor = (17 * contador)
			if pstCom == "I":
				valor = (18 * contador)
			if pstCom == "J":
				valor = (19 * contador)
			if pstCom == "K":
				valor = (20 * contador)
			if pstCom == "L":
				valor = (21 * contador)
			if pstCom == "M":
				valor = (22 * contador)
			if pstCom == "N":
				valor = (23 * contador)
			if pstCom == "Ñ":
				valor = (24 * contador)
			if pstCom == "O":
				valor = (25 * contador)
			if pstCom == "P":
				valor = (26 * contador)
			if pstCom == "Q":
				valor = (27 * contador)
			if pstCom == "R":
				valor = (28 * contador)
			if pstCom == "S":
				valor = (29 * contador)
			if pstCom == "T":
				valor = (30 * contador)
			if pstCom == "U":
				valor = (31 * contador)
			if pstCom == "V":
				valor = (32 * contador)
			if pstCom == "W":
				valor = (33 * contador)
			if pstCom == "X":
				valor = (34 * contador)
			if pstCom == "Y":
				valor = (35 * contador)
			if pstCom == "Z":
				valor = (36 * contador)

			contador = contador - 1
			count = count + 1
			sumaria = sumaria + valor


		# Sacar el residuo	
		numVerificador = sumaria % 10
		# Devuelve el valor absoluto en caso de que sea negativo
		numVerificador = abs(10 - numVerificador)
		#En caso de que sea 10 el digito es 0
		if numVerificador == 10:
			numVerificador = 0
		# Obtener homoclave
		if anio < 2000:
			homoclave = "0" + ""
		elif anio >= 2000:
			homoclave = "A" + ""

		curp = curp + homoclave + str(numVerificador)
		return curp	

	def calculaHomoclaveRFC(rfc, nombre_completo):

		valorSuma = 0 
		
		dic1 = {" ":0 ,"&":10,"A":11,"B":12,"C":13,"D":14,"E":15,"F":16,"G":17,"H":18,"I":19,"J":21,"K":22,"L":23,"M":24,"N":25,"O":26,"P":27,"Q":28,"R":29,
			"S":32,"T":33,"U":34,"V":35,"W":36,"X":37,"Y":38,"Z":39,"Ñ":40,"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
		}
		dic2 = {0:"1",1:"2",2:"3",3:"4",4:"5",5:"6",6:"7",7:"8",8:"9",9:"A",0:"B",1:"C",2:"D",3:"E",4:"F",5:"G",6:"H",7:"I",8:"J",9:"K",0:"L",1:"M",2:"N",
			3:"P",4:"Q",5:"R",6:"S",7:"T",8:"U",9:"V",0:"W",1:"X",2:"Y",3:"Z",
		}
		
		dic3 = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"&":24,"O":25,"P":26,"Q":27,"R":28,"S":29,
			"T":30,"U":31,"V":32,"W":33,"X":34,"Y":35,"Z":36," ":37,"Ñ":38,"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
		}
	
		list_num = [0]
		for item in nombre_completo:
			for key, value in dic1.items():
				if item == key:
					list_num.append(value)
				else:
					list_num.append(00)

		count = 0
		for num in list_num:
			count = count+1
			valorSuma += (num * 10) + (num + 1) * (num + count)


		div = 0 
		mod = 0
		div = valorSuma % 1000
		mod = div % 34
		div = (div - mod) / 34

		indice = 0
		hc = ""

		while (indice <= 1):
			for key, value in dic2.items():
				if indice == key:
					hc += value
			indice = indice + 1

		#Agregamos al RFC los dos primeros caracteres de la homoclave
		rfc += hc

		rfcAnumeroSuma = 0 
		sumaParcial = 0

		count = 0
		for c in rfc:
			count = count + 1
			for key, value in dic3.items():
				if c == key:
					rfcAnumeroSuma = value
					sumaParcial += (rfcAnumeroSuma * (14 - (count + 1)))


		moduloVerificador = sumaParcial % 11
		if (moduloVerificador == 0):
			rfc += "0"
		else:
			sumaParcial = 11 - moduloVerificador
			if (sumaParcial == 10):
				rfc += "A"
			else:
				rfc += str(sumaParcial)

		return rfc


	def getConsonante(curp, param):
		consonante = ""
		if param != "":
			consonante = Utils.getConsonateCurp(param)
			if consonante != "":
				curp = curp + consonante
			else:
				constante = "X";
				curp = curp + constante
		else:
			curp = curp + "X"

		return curp