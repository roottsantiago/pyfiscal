"""
File manages validator tests
"""
import unittest

from pyfiscal.helpers import DataFiscalValidator
from pyfiscal.validators import validate_curp, validate_nss, validate_rfc

validator = DataFiscalValidator()


class ValidatorTestCase(unittest.TestCase):
    """
    Validator testing class.
    """
    curp = 'SABC560626MDFLRN01'
    social_security_number = '72795608040'
    rfc = 'JUMM420313PA9'

    def test_validate_format_curp(self):
        """
        Validation of the curp format.
        """
        is_valid = validate_curp(self.curp)
        self.assertTrue(is_valid, 'The curp does not have the valid format.')

    def test_validate_digit_curp(self):
        """
        Validation of the curp check digit.
        """
        self.assertEqual(
            validator.check_digit_curp(self.curp[0:17]),
            self.curp[-1], 'The check digit is not correct'
        )

    def test_validate_format_nss(self):
        is_valid = validate_nss(self.social_security_number)
        self.assertTrue(is_valid, 'The NSS does not have the valid format.')

    def test_validate_nss(self):
        is_valid = validator.check_nss_registration_date(self.social_security_number)
        self.assertTrue(is_valid, 'Discharged before birth')
        
    def test_validate_digit_nss(self):
        """
        Validation of the NSS check digit.
        """
        is_valid = validator.check_digit_nss(self.social_security_number)
        self.assertTrue(is_valid, 'The check digit is not correct')

    def test_validate_format_rfc(self):
        """
        Validation of the RFC format.
        """
        is_valid = validate_rfc(self.rfc)
        self.assertTrue(is_valid, 'The RFC does not have the valid format.')


if __name__ == '__main__':
    unittest.main()
