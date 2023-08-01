# Calculation of tax data in México

Features
[x] Support for Python 2.7-3.5.

Installation
------------

Install pyfiscal.
```python
pip install pyfiscal
```

#  CURP

The Clave Única de Registro de Población (CURP) is a unique 18 character alphanumeric identity code for both Mexican residents and citizens.

![alt picture](https://github.com/thomgonzalez/pyfiscal/blob/master/img/CURP.jpg)


# RFC

The Federal Taxpayer Registry is a code used in Mexico to distinguish each individual or company required to pay taxes. The people or organizations that have their RFC are called contributors.

1.- Para la Persona Física:

![alt picture](https://github.com/thomgonzalez/pyfiscal/blob/master/img/RFC.jpg)

This homoclave will be designated by the SAT, reviewing the request through already designated official paper.


# NSS

The Social Security Number (NSS) is unique, permanent and nontransferable and is assigned to keep a record of workers and insured.

![alt picture](https://github.com/thomgonzalez/pyfiscal/blob/master/img/NSS.png)

Validation:
* Only 11 digits will be validated.
* Validation by the Luhn algorithm.
* Calculate the last digit.


# Unit Tests
```python

python -m unittest tests/data_fiscal_test.py

python -m unittest tests/validator_test.py 

```

License
-------

See LICENSE for more details (The MIT License).


References
----------

https://es.wikipedia.org/wiki/Algoritmo_de_Luhn
