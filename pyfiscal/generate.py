# -*- coding: utf-8 -*-
"""
Base file in the generation and calculation of fiscal data.
"""
from .base import BaseGenerator
from .constants import TABLE1, TABLE2, TABLE3


# pylint: disable=W0223
class GenerateRFC(BaseGenerator):
    """
    Base class that generate RFC
    """
    key_value = 'rfc'
    DATA_REQUIRED = ('complete_name', 'last_name',
                     'mother_last_name', 'birth_date')
    partial_data = None

    def __init__(self, **kwargs):
        self.complete_name = kwargs.get('complete_name')
        self.last_name = kwargs.get('last_name')
        self.mother_last_name = kwargs.get('mother_last_name')
        self.birth_date = kwargs.get('birth_date')

        self.parse(complete_name=self.complete_name, last_name=self.last_name,
                   mother_last_name=self.mother_last_name)

        self.partial_data = self.data_fiscal(
            complete_name=self.complete_name, last_name=self.last_name,
            mother_last_name=self.mother_last_name, birth_date=self.birth_date)

    def calculate(self):
        """
        Calculation method
        """
        rfc = self.partial_data
        rfc += self.homoclave(self.full_name)
        rfc += self.verification_number(rfc)
        return rfc

    @staticmethod
    def homoclave(full_name):
        """
        Method that calculates the homoclave
        """
        num = '0'
        summary = 0
        div = 0
        mod = 0

        # 1.- Values will be assigned to the letters of the name or
        # business name according to the table1
        # 2.- The values are ordered as follows:
        # G O M E Z D I A Z E M M A
        # 017 26 24 15 39 00 14 19 11 39 00 15 24 24 11
        # A zero is added to the value of the first letter to standardize
        # the criteria of the numbers to be taken two by two.
        len_full_name = len(full_name)
        for index in range(len_full_name):
            rfc1 = dict((x, y) for x, y in TABLE1)
            num += rfc1.get(full_name[index])

        # 3. The multiplications of the numbers taken two by two for
        # the position of the couple will be carried out:
        # La formula es:
            # El caracter actual multiplicado por diez mas el valor del caracter
            # siguiente y lo anterior multiplicado por el valor del caracter
            # siguiente.
        count = 0
        for index in range(len(num) - 1):
            count += 1
            summary += ((int(num[index]) * 10) + int(num[count]))\
                * int(num[count])

        # 4.- The result of the multiplications is added and the result
        # obtained, the last three figures will be taken and these are divided
        # by the factor 34.
        div = summary % 1000

        # mod = div % 34
        # div = (div-mod)/34
        div, mod = divmod(div, 34)
        # 5. With the quotient and the remainder, the table 2 is consulted
        # and the homonymy is assigned.
        rfc2 = dict((x, y) for x, y in TABLE2)
        hom = ''
        hom += rfc2.get(int(div))
        hom += rfc2.get(int(mod))
        return hom

    @staticmethod
    def verification_number(rfc):
        """
        Anexo 3 - Tabla de valores para la generación del código verificador
        del registro federal de contribuyentes.
        """
        num = 0
        sumparcial = 0
        digito = None

        # 2.- Una vez asignados los valores se aplicará la siguiente forma
        # tomando como base el factor 13
        # en orden descendente a cada letra y número del R.F.C.
        # para su multiplicación, de acuerdo a la siguiente formula:
        # (Vi * (Pi + 1)) + (Vi * (Pi + 1)) + ..............+ (Vi * (Pi + 1))
        # MOD 11
        rfc3 = dict((x, y) for x, y in TABLE3)

        lenrfc = len(rfc)
        for count in range(lenrfc):
            letra = rfc[count]

            if rfc3.get(letra):
                num = rfc3.get(letra)
                sumparcial += (int(num) * (14 - (count + 1)))

        # 3.- El resultado de la suma se divide entre el factor 11.

        # Si el residuo es igual a cero, este será el valor que se le asignará
        # al dígito verificador.
        # Si el residuo es mayor a cero se restará este al factor 11: 11-3 =8
        # Si el residuo es igual a 10 el dígito verificador será “ A”.
        # Si el residuo es igual a cero el dígito verificador será cero.
        # Por lo tanto “8“
        # es el dígito verificador de este ejemplo: GODE561231GR8.

        residuo = sumparcial % 11

        if residuo == 0:
            digito = '0'
            return digito

        if residuo > 0:
            digito = str((11 - residuo))

            if digito == '10':
                digito = 'A'
                return digito

            return digito

        return digito

    @property
    def data(self):
        """
        Property method
        """
        return self.calculate()


# pylint: disable=W0223
class GenerateCURP(BaseGenerator):
    """ Generate CURP"""
    key_value = 'curp'
    partial_data = None
    DATA_REQUIRED = (
        'complete_name',
        'last_name',
        'mother_last_name',
        'birth_date',
        'gender',
        'city',
        'state_code'
    )

    def __init__(self, **kwargs):
        self.complete_name = kwargs.get('complete_name')
        self.last_name = kwargs.get('last_name')
        self.mother_last_name = kwargs.get('mother_last_name', None)
        self.birth_date = kwargs.get('birth_date')
        self.gender = kwargs.get('gender')
        self.city = kwargs.get('city', None)
        self.state_code = kwargs.get('state_code')

        self.parse(complete_name=self.complete_name, last_name=self.last_name,
                   mother_last_name=self.mother_last_name, city=self.city,
                   state_code=self.state_code)

        self.partial_data = self.data_fiscal(
            complete_name=self.complete_name, last_name=self.last_name,
            mother_last_name=self.mother_last_name, birth_date=self.birth_date)

    def calculate(self):
        """
        Method that calculate the RFC
        """
        curp = self.partial_data

        state_code = (self.city_search(self.city)
                      if self.city else self.state_code)
        if not state_code:
            raise AttributeError("No such attribute: state_code")

        lastname = self.get_consonante(self.last_name)
        mslastname = self.get_consonante(self.mother_last_name)
        name = self.get_consonante(self.complete_name)
        year = self.get_year(self.birth_date)
        hcv = self.homoclave(year)

        curp += f'{self.gender}{state_code}{lastname}{mslastname}{name}{hcv}'
        curp += self.check_digit(curp)
        return curp

    @staticmethod
    def homoclave(year):
        """
        Method that obtain the homoclave
        """
        hcv = ''
        if year < 2000:
            hcv = '0'
        elif year >= 2000:
            hcv = 'A'
        return hcv

    @staticmethod
    def check_digit(curp):
        """
        Check and get the digit
        """
        value = 0
        summary = 0
        checkers = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
            'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
            'M': 22, 'N': 23, 'Ñ': 24, 'O': 25, 'P': 26, 'Q': 27, 'R': 28,
            'S': 29, 'T': 30, 'U': 31, 'V': 32, 'W': 33, 'X': 34, 'Y': 35,
            'Z': 36
        }

        count2 = 18
        lencurp = len(curp)

        for index in range(lencurp):
            posicion = curp[index]
            for k, v in checkers.items():
                if posicion == k:
                    value = (v * count2)
            count2 = count2 - 1
            summary = summary + value
        # Residue
        num_ver = summary % 10
        # Returns the absolute value in case it is negative.
        num_ver = abs(10 - num_ver)
        num_ver = 0 if num_ver == 10 else num_ver
        return str(num_ver)

    @property
    def data(self):
        """
        Property method
        """
        return self.calculate()


# pylint: disable=W0223
class GenerateNSS(BaseGenerator):
    """
    Class that calculates the NNS
    """
    def __init__(self, nss):
        self.nss = nss

    def is_valid(self):
        """
        Validation method
        """
        # 11 dígitos y subdelegación válida
        if not len(self.nss) == 11:
            return False

        sub_deleg = int(self.nss[0:2])
        year = self.current_year() % 100
        high_date = int(self.nss[2:4])
        birth_date = int(self.nss[4:6])

        if sub_deleg != 97:
            if high_date <= year:
                high_date += 100
            if birth_date <= year:
                birth_date += 100
            if birth_date > high_date:
                raise Exception("Error: He was discharged before he was born.")

        return self._is_luhn_valid()

    def _is_luhn_valid(self):
        """
        Validate an entry with a check digit.
        Example 4896889802135
        """
        num = list(map(int, str(self.nss)))
        return (sum(num[::-2] + [sum(divmod(d * 2, 10))
                                 for d in num[-2::-2]]) % 10 == 0)

    def _calculate_luhn(self):
        """
        Calculation of said digit.
        """
        num = list(map(int, str(self.nss)))
        check_digit = (10 - sum(num[-2::-2] + [sum(divmod(d * 2, 10))
                                               for d in num[::-2]]) % 10)
        return 0 if check_digit == 10 else check_digit

    @property
    def data(self):
        """
        Property data
        """
        return self._calculate_luhn()


class GenericGeneration:
    """
    Class Generic Generation
    """
    _data = {}
    generators = ()

    def __init__(self, **kwargs):
        self._datos = kwargs

    @property
    def data(self):
        """
        Property data
        """
        for cls in self.generators:
            data = cls.DATA_REQUIRED
            kargs = {key: self._datos[key] for key in data}
            gen = cls(**kargs)
            gen.calculate()
            self._data[gen.key_value] = gen.data

        return self._data


class GenerateDataFiscal(GenericGeneration):
    """
    RFC and CURP generation
    """
    generators = (GenerateCURP, GenerateRFC)
