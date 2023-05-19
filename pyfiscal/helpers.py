"""
Script that manages tax data helpers
"""
from .constants import CHECKERS, TABLE3
from .utils import get_current_year


class DataFiscalValidator:
    """
    Data fiscal validator class
    """
    @staticmethod
    def check_digit_curp(curp: str) -> str:
        """
        Method get check digit
        """
        value = 0
        summary = 0
        count = 18
        len_curp = len(curp)

        for index in range(len_curp):
            for key, val in CHECKERS.items():
                value = val if curp[index] == key else value
            summary = summary + value * count
            count -= 1

        # Get residue and returns the absolute value in case it is negative.
        digit = abs(10 - (summary % 10))
        digit = 0 if digit == 10 else digit
        return str(digit)

    @staticmethod
    def check_digit_rfc(rfc: str) -> str:
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

    @staticmethod
    def check_nss_registration_date(nss: str) -> bool:
        """Compare years except you don't have birth year

        11 digits and valid subdelegation
        """
        subdelegation = int(nss[0:2])
        year = get_current_year() % 100
        high_date = int(nss[2:4])
        birth_date = int(nss[4:6])

        if subdelegation != 97:
            if high_date <= year:
                high_date += 100
            if birth_date <= year:
                birth_date += 100
            if birth_date > high_date:
                # He was discharged before he was born
                return False
        return True

    @staticmethod
    def check_digit_nss(nss):
        """
        Validate an entry with a check digit.
        Example 4896889802135
        """
        num = list(map(int, str(nss)))
        data = (sum(num[::-2] + [sum(divmod(d * 2, 10))
                                 for d in num[-2::-2]]) % 10 == 0)
        return data
