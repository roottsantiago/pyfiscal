from utils import *
from stringBuilder import*


class General:

	def datosGenerales(nombre, ape_paterno, ape_materno, fecha_nacimiento):
		generico = ""
		
		# Regresa Curp y RFC
		generico = General.calculaOrigenCurp(nombre, ape_paterno, ape_materno)

		# Verificar los datos que no tenga palabras obsenas 
		generico = Utils.verificarPalabras(generico)

		# Agregamos la fecha de Nacimiento
		generico = Utils.fechaNacimiento(generico, fecha_nacimiento)
		return generico

	def calculaOrigenCurp(nombre, apellidoPaterno, apellidoMaterno):
		curp = ""
		
		# No tiene Apellido Paterno
		if apellidoPaterno == "" and apellidoMaterno != "":
			#Agregamos el primer caracter del apellido paterno
			curp = "XX"
			curp += apellidoMaterno[0:2]

		# No tiene Apellido Materno 
		if apellidoMaterno == "" and apellidoPaterno != "":
			#Agregamos el primer caracter del apellido paterno
			curp = apellidoPaterno[0:1]
			z1 = len(apellidoPaterno) - 1
			apePaterno = apellidoPaterno[1:z1]
			#Buscamos y agregamos al curp la primera vocal del apellido
			for item in apePaterno:
				if Utils.esVocal(item):
					curp += item
					break

			curp += "X"
			#Armar letras del nombre
			curp += nombre[0:1]

		if apellidoPaterno != "" and apellidoMaterno != "":
			#Agregamos el primer caracter del apellido paterno
			curp = apellidoPaterno[0:1]
			z1 = len(apellidoPaterno) - 1
			apePaterno = apellidoPaterno[1:z1]

			#Buscamos y agregamos al curp la primera vocal del primer apellido
			for item in apePaterno:
				if Utils.esVocal(item):
					curp += item
					break
			curp += apellidoMaterno[0:1]
			 #Agregamos el primer caracter del primer nombre
			curp += nombre[0:1]

		return curp

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

		for count in range(0,len(curp)):
			pstCom = curp[count]

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
		# Guardara el nombre en su correspondiente numérico
		nombreEnNumero = ""
		# La suma de la secuencia de números de nombreEnNumero
		valorSuma = 0 

		# Diccionarios para calcular la homoclave
		dic1_rfc = {
			" ":00 ,"&":10,"Ñ":10,"A":11,"B":12,
			"C":13,"D":14,"E":15,"F":16,"G":17,
			"H":18,"I":19,"J":21,"K":22,"L":23,
			"M":24,"N":25,"O":26,"P":27,"Q":28,
			"R":29,"S":32,"T":33,"U":34,"V":35,
			"W":36,"X":37,"Y":38,"Z":39,"0":0,
			"1":1,"2":2,"3":3,"4":4,"5":5,
			"6":6,"7":7,"8":8,"9":9,
		}

		dic2_rfc = {
			0:"1",1:"2",2:"3",3:"4",4:"5",
			5:"6",6:"7",7:"8",8:"9",9:"A",
			10:"B",11:"C",12:"D",13:"E",14:"F",
			15:"G",16:"H",17:"I",18:"J",19:"K",
			20:"L",21:"M",22:"N",23:"P",24:"Q",
			25:"R",26:"S",27:"T",28:"U",29:"V",
			30:"W",31:"X",32:"Y",
		}
		
		dic3_rfc = {
			"A":10,"B":11,"C":12,"D":13,"E":14,
			"F":15,"G":16,"H":17,"I":18,"J":19,
			"K":20,"L":21,"M":22,"N":23,"O":25,
			"P":26,"Q":27,"R":28,"S":29,"T":30,
			"U":31,"V":32,"W":33,"X":34,"Y":35,
			"Z":36,"0":0,"1":1,"2":2,"3":3,
			"4":4,"5":5,"6":6,"7":7,"8":8,
			"9":9,"" :24," ":37,
		}
		# Agregamos un cero al inicio de la representación númerica del nombre
		nombreEnNumero = "0"

		# Recorremos el nombre y vamos convirtiendo las letras en su valor numérico
		for count in range(0,len(nombre_completo)):
			c = nombre_completo[count] 
			nombreEnNumero += Utils.rfcSet(str(dic1_rfc[c]),"00")

		# La formula es:
            # El caracter actual multiplicado por diez mas el valor del caracter siguiente y 
            # lo anterior multiplicado por el valor del caracter siguiente
		for count in range(0,len(nombreEnNumero)-1):
			count2 = count+1
			valorSuma += ((int(nombreEnNumero[count])*10) + int(nombreEnNumero[count2])) * int(nombreEnNumero[count2])

		# Definicion default	
		div = 0 
		mod = 0
		div = valorSuma % 1000
		mod = div % 34
		div = (div - mod) / 34

		# Los dos primeros caracteres de la homoclave
		hc = ""
		hc += Utils.rfcSet(dic2_rfc[int(div)],"Z")
		hc += Utils.rfcSet(dic2_rfc[int(mod)],"Z")

		#Agregamos al RFC los dos primeros caracteres de la homoclave
		rfc += hc

		# Aqui empieza el calculo del digito verificador basado en lo que tenemos del RFC
		rfcAnumeroSuma = 0 
		sumaParcial = 0

		for count in range(0,len(rfc)):
			c = rfc[count]
			if dic3_rfc[c]:
				rfcAnumeroSuma = dic3_rfc[c]
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

	def consonante(curp, param):
		consonante = ""
		if param != "":
			consonante = Utils.getConsonateCurp(param)
			if consonante != "":
				curp = curp + consonante
			else:
				constante = "X"
				curp = curp + constante
		else:
			curp = curp + "X"

		return curp
