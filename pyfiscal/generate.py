# -*- coding: utf-8 -*-
"""
Base file in the generation and calculation of fiscal data.
"""
from .base import BaseGenerator
from .constants import TABLE1, TABLE2, TABLE3, CHECKERS
from .utils import GenderEnum


# pylint: disable=W0223
class GenerateRFC(BaseGenerator):
    """
    Base class that generate RFC
    """
    partial_data = None
    key_value = 'rfc'
    DATA_REQUIRED = (
        'name',
        'last_name',
        'mother_last_name',
        'birth_date'
    )

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.last_name = kwargs.get('last_name')
        self.mother_last_name = kwargs.get('mother_last_name')
        self.birth_date = kwargs.get('birth_date')

        self.parse(name=self.name, last_name=self.last_name,
                   mother_last_name=self.mother_last_name)

        self.partial_data = self.data_fiscal(
            name=self.name,
            last_name=self.last_name,
            mother_last_name=self.mother_last_name,
            birth_date=self.birth_date
        )

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
        digit = None

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

        residue = sumparcial % 11
        digit = '0' if residue == 0 else residue

        if int(digit) > 0:
            digit = 11 - residue
            digit = 'A' if digit == 10 else digit
        return str(digit)

    @property
    def data(self):
        """
        Property method
        """
        return self.calculate()


# pylint: disable=W0223
class GenerateCURP(BaseGenerator):
    """
    Generate CURP
    """
    partial_data = None
    key_value = 'curp'
    DATA_REQUIRED = (
        'name',
        'last_name',
        'mother_last_name',
        'birth_date',
        'gender',
        'state'
    )

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.last_name = kwargs.get('last_name')
        self.mother_last_name = kwargs.get('mother_last_name', None)
        self.birth_date = kwargs.get('birth_date')
        self.gender = kwargs.get('gender')
        self.state = kwargs.get('state')

        self.parse(name=self.name, last_name=self.last_name,
                   mother_last_name=self.mother_last_name,state=self.state)

        self.partial_data = self.data_fiscal(
            name=self.name,
            last_name=self.last_name,
            mother_last_name=self.mother_last_name,
            birth_date=self.birth_date
        )

    def calculate(self):
        """
        Method that calculate the CURP
        """
        if not self.state:
            raise AttributeError("No such attribute: state")

        if not self.gender:
            raise AttributeError("No such attribute: gender")

        gender = self.get_gender(self.gender)
        state_code = (self.get_federative_entity(self.state)
                      if self.state else None)
        last_name = self.get_consonant(self.last_name)
        mother_last_name = self.get_consonant(self.mother_last_name)
        name = self.get_consonant(self.complete_name)
        homoclave = self.homoclave(self.get_year(self.birth_date))

        curp = self.partial_data
        curp += f'{gender}{state_code}{last_name}{mother_last_name}'\
            f'{name}{homoclave}'
        curp += self.check_digit(curp)
        return curp

    @staticmethod
    def get_gender(gender: str):
        """
        Get gender of enum
        """
        value = None
        try:
            gender = gender.upper()
            value = GenderEnum[gender].value
        except KeyError as exc:
            print('Value not found in gender enum', exc)
        return value

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
        count = 18
        len_curp = len(curp)

        for index in range(len_curp):
            posicion = curp[index]
            for k, v in CHECKERS.items():
                if posicion == k:
                    value = (v * count)
            count = count - 1
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
    Base class that calculates the social security number
    """
    def __init__(self, nss):
        self.nss = nss

    def is_valid(self):
        """Validation method

        11 digits and valid subdelegation
        """
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
        Property method
        """
        return self._calculate_luhn()


class GenericGeneration:
    """
    Class Generic Generation
    """
    _data = {}
    generators = ()

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    @property
    def data(self):
        """
        Property method
        """
        for cls in self.generators:
            data = cls.DATA_REQUIRED
            kwargs = {key: self._kwargs[key] for key in data}
            gen = cls(**kwargs)
            gen.calculate()
            self._data[gen.key_value] = gen.data

        return self._data


class GenerateDataFiscal(GenericGeneration):
    """
    RFC and CURP generation
    """
    generators = (GenerateCURP, GenerateRFC)
