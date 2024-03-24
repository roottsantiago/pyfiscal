# Calculation of tax data in México

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/sutsantiago/pyfiscal/blob/master/LICENSE.txt)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Installation

Install pyfiscal.
```python
pip install pyfiscal
```

CURP
----
The Clave Única de Registro de Población (CURP) is a unique 18 character alphanumeric identity code for both Mexican residents and citizens.

![alt picture](https://github.com/roottsantiago/pyfiscal/blob/master/img/CURP.jpg)


RFC
---
The Federal Taxpayer Registry is a code used in Mexico to distinguish each individual or company required to pay taxes. The people or organizations that have their RFC are called contributors.

1.- Physical person:

![alt picture](https://github.com/roottsantiago/pyfiscal/blob/master/img/RFC.jpg)

This homoclave will be designated by the SAT, reviewing the request through already designated official paper.


NSS
---
The Social Security Number (NSS) is unique, permanent and nontransferable and is assigned to keep a record of workers and insured.

![alt picture](https://github.com/roottsantiago/pyfiscal/blob/master/img/NSS.png)

Validation:
* Only 11 digits will be validated.
* Validation by the Luhn algorithm.
* Calculate the last digit.


## Getting Started with Docker
If you want to install the dependencies and work using Docker, you can simply follow this steps. 

Clone the project repository
```bash
git clone https://github.com/roottsantiago/pyfiscal.git
cd pyfiscal
```

### Usage
There are several ways to use the project because there are those using `docker-compose.yml` and `Dockerfile`. Here's how to use it:

> This is for the install part with docker-compose
```compose
# Build
docker-compose build
# Run
docker-compose up -d
````

## Unit Tests
```python
python -m unittest tests/data_fiscal_test.py
python -m unittest tests/validator_test.py
```
> Testing with docker
```python
docker exec pyfiscal python -m unittest tests/data_fiscal_test.py
docker exec pyfiscal python -m unittest tests/validator_test.py
```
## License

See LICENSE for more details (The MIT License).


## References

https://es.wikipedia.org/wiki/Algoritmo_de_Luhn
