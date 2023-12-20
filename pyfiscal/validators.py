"""
Script manages tax data validators
"""
import re
from datetime import datetime


class ValidationError(Exception):
    """
    Base class for all exceptions.
    """
    default = "Format: Invalid"


def validate_curp(value):
    """
    CURP validator method
    """
    PATTERN_CURP = "^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d" \
        "|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|" \
        "Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$"
    message = 'Does not match the format of a CURP'
    regex = re.compile(PATTERN_CURP)

    if not regex.match(value):
        raise ValidationError(message)

    return True


def validate_nss(value):
    """
    Social security number (NSS) validator
    """
    PATTERN_NSS = "^(\d{2})(\d{2})(\d{2})\d{5}$"
    message = 'Does not match the format of a NSS'
    regex = re.compile(PATTERN_NSS)

    if not regex.match(value):
        raise ValidationError(message)

    return True


def validate_rfc(value):
    """
    RFC validator
    """
    PATTERN_RFC = "^(([A-ZÑ&]{4})([0-9]{2})([0][13578]|[1][02])" \
        "(([0][1-9]|[12][\\d])|[3][01])([A-Z0-9]{3}))|(([A-ZÑ&]{4})([0-9]{2})" \
        "([0][13456789]|[1][012])(([0][1-9]|[12][\\d])|[3][0])([A-Z0-9]{3}))|" \
        "(([A-ZÑ&]{4})([02468][048]|[13579][26])[0][2]([0][1-9]|[12][\\d])" \
        "([A-Z0-9]{3}))|(([A-ZÑ&]{4})([0-9]{2})[0][2]" \
        "([0][1-9]|[1][0-9]|[2][0-8])([A-Z0-9]{3}))$"
        
    message = 'Does not match the format of a RFC'
    regex = re.compile(PATTERN_RFC)

    if not regex.match(value):
        raise ValidationError(message)

    return True


def validate_date(value: str):
    """
    Try to parse a date using several formats, warn about
    problematic value if the possible_date does not match
    any of the formats tried
    """
    FORMATS_DATE_FIELD = ('%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y', '%Y/%m/%d')
    for fmt in FORMATS_DATE_FIELD:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass
    mesage = f"Non-valid date format found: '{value}'"
    raise ValidationError(mesage)
