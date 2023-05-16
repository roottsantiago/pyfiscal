"""
Test file
"""
from pyfiscal.pyfiscal.generate import (
    GenerateRFC,
    GenerateCURP,
    GenerateNSS,
    GenerateDataFiscal
)


kwargs = {
    "complete_name": "Tomas",
    "last_name": "Santiago",
    "mother_last_name": "Gonzalez",
    "birth_date": "16-11-1989",
    "gender": "M",
    "city": "",
    "state_code": "HG"
}

rfc = GenerateRFC(**kwargs)
data = rfc.data
print(data)
curp = GenerateCURP(**kwargs)
data = curp.data
print(data)
nss = GenerateNSS(nss="")
data = nss.data
print(data)
data = GenerateDataFiscal(**kwargs).data
print(data)
