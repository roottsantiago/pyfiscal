# -*- coding: utf-8 -*-
"""
Base file in the generation and calculation of fiscal data.
"""
from .base import BaseGenerator
from .helpers import DataFiscalValidator


from .constants import TABLE1, TABLE2
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
        validator = DataFiscalValidator()
        rfc = self.partial_data
        rfc += self.homoclave(self.full_name)
        rfc += validator.check_digit_rfc(rfc)
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
                   mother_last_name=self.mother_last_name, state=self.state)

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
        validator = DataFiscalValidator

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
        curp += validator.check_digit_curp(curp)
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
