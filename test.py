# -*- coding: utf-8 -*-
from generate import GenerateRFC, GenerateCURP, GenerateNSS, GenericGeneration


class GenerateDataFiscal(GenericGeneration):
	generadores = (GenerateCURP, GenerateRFC)


kwargs = {
	"complete_name": "Thom",
	"last_name": "Gonzalez",
	"mother_last_name": None,
	"birth_date": "01-01-1990",
	"gender": "H",
	"city": 'Queretaro',
	"state_code": None
}

rfc = GenerateRFC(**kwargs)
print(rfc.data)

curp = GenerateCURP(**kwargs)
print(curp.data)

nss =  GenerateNSS(nss='2812890481')
print(nss.is_valid())

data = nss.data
print(data)

data = GenerateDataFiscal(**kwargs).data
print(data)
