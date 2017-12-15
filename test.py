# -*- coding: utf-8 -*-
from calcule import CalculeRFC, CalculeCURP, CalculeNSS, CalculeGeneric


class GenerateDataFiscal(CalculeGeneric):
	generadores = (CalculeCURP, CalculeRFC)


kwargs = {
	"complete_name": "Thom",
	"last_name": "Gonzalez",
	"mother_last_name": None,
	"birth_date": "01-01-1990",
	"gender": "H",
	"city": 'Queretaro',
	"state_code": None
}

rfc = CalculeRFC(**kwargs).data
#print(rfc)

curp = CalculeCURP(**kwargs).data
#print(curp)

calc =  CalculeNSS(nss='2812890481')
#print(calc.is_valid())

digit = calc.digit()
#print(digit)

data = GenerateDataFiscal(**kwargs).data
#print(data)
