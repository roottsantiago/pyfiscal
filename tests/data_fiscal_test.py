"""
Test file
"""
import unittest
from pyfiscal.generate import (
    GenerateRFC,
    GenerateCURP,
    GenerateNSS,
    GenerateDataFiscal
)


class DataFiscalTestCase(unittest.TestCase):
    """
    Test class for tax data.
    """
    DFT = {'curp': 'GODE561231MHGMZM07', 'rfc': 'GODE561231GR8'}

    rfc_params = {
        'name': 'Luz María',
        'last_name': 'Fernández',
        'mother_last_name': 'Juárez',
        'birth_date': '05-02-2020'
    }

    curp_params = {
        'name': 'Concepción',
        'last_name': 'Salgado',
        'mother_last_name': 'Briseño',
        'birth_date': '26-06-1956',
        'gender': 'Mujer',
        'state': 'Distrito Federal'
    }

    params = {
        'name': 'Emma',
        'last_name': 'Gómez',
        'mother_last_name': 'Díaz',
        'birth_date': '31-12-1956',
        'gender': 'Mujer',
        'state': 'Hidalgo'
    }

    def test_generate_rfc(self):
        """
        Method that calculates RFC
        """
        rfc = GenerateRFC(**self.rfc_params).data
        print(f'RFC: {rfc}')
        self.assertEqual(len(rfc), 13, 'The length of the RFC is not valid.')

    def test_generate_curp(self):
        """
        Method that calculates CURP
        """
        curp = GenerateCURP(**self.curp_params).data
        print(f'CURP: {curp}')
        self.assertEqual(len(curp), 18, 'The length of the CURP is not valid.')

    def test_digit_nns(self):
        """
        Method gets the digit of the social security number
        """
        nss = GenerateNSS(nss="7279560804").data
        self.assertTrue(str(nss).isdigit(), 'It is not a valid digit.')

    def test_generate_data_fiscal(self):
        """
        Get tax data
        """
        data = GenerateDataFiscal(**self.params).data
        self.assertDictEqual(self.DFT, data)


if __name__ == '__main__':
    unittest.main()
