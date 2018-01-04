# Cálculo de Datos Fiscales

Features
[x] Support for Python 2.7-3.3.

Installation
------------

Install pyfiscal.
```python
pip install pyfiscal
```

#  CURP

La Clave Única de Registro de Población (CURP) es un código alfanumérico único de identidad de 18 caracteres, tanto para residentes como para ciudadanos mexicanos.

![alt picture](https://github.com/thomgonzalez/pyfiscal/blob/master/img/CURP.jpg)


# RFC

El Registro Federal de Contribuyentes es una clave que se usa en México para distinguir a cada individuo o empresa obligado a pagar impuestos. A las personas u organizaciones que cuentan con su RFC se les llama contribuyentes.

1.- Para la Persona Física:

![alt picture](https://github.com/thomgonzalez/pyfiscal/blob/master/img/RFC.jpg)

Esta homoclave la designará el SAT, revisando la petición a través de papel oficial ya designado.


# NSS

El Número de Seguridad Social (NSS) es único, permanente e intransferible y se asigna para llevar un registro de los trabajadores y asegurados.

![alt picture](https://github.com/thomgonzalez/pyfiscal/blob/master/img/NSS.png)

1.- Validación Completa:
* Sólo se validará que sean 11 dígitos.
* Validación por el algoritmo de Luhn.
* Cálcula el último dígito.


# Example
```python
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
data = rfc.data

curp = GenerateCURP(**kwargs)
data = curp.data

nss =  GenerateNSS(nss='2812890481')
data = nss.data

data = GenerateDataFiscal(**kwargs).data

```

License
-------

See LICENSE for more details (The MIT License).


References
----------

https://es.wikipedia.org/wiki/Algoritmo_de_Luhn
