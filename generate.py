# -*- coding: utf-8 -*-

from calcule import CalculeRFC, CalculeCURP, CalculeGeneric

class GenerateDataFiscal(CalculeGeneric):
	generadores = (CalculeCURP, CalculeRFC)

	