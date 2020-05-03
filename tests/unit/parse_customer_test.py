from unittest import TestCase

from salesdataanalyzer.helpers import Customer
from salesdataanalyzer.parser import parse_customer, \
    WrongNumberOfFieldsError, InvalidCnpjPatternError


class ParseCustomerTest(TestCase):
    def test_parse_customer(self):
        customer = parse_customer('002ç12312312312312çDale CarnegieçFarming')

        self.assertEqual(Customer('12312312312312',
                                  'Dale Carnegie',
                                  'Farming'),
                         customer)

    def test_raise_wrong_number_of_fields_error_for_missing_field(self):
        self.assertRaises(WrongNumberOfFieldsError,
                          parse_customer,
                          '002ç12312312312312çDale Carnegie')

    def test_raise_wrong_number_of_fields_error_for_extra_field(self):
        self.assertRaises(WrongNumberOfFieldsError,
                          parse_customer,
                          '002ç12312312312312çDale CarnegieçFarmingç'
                          'Extra Field')

    def test_raise_invalid_cnpj_pattern_error_for_invalid_characters(self):
        self.assertRaises(InvalidCnpjPatternError,
                          parse_customer,
                          '002ç123abc12312312çDale CarnegieçFarming')

    def test_raise_invalid_cnpj_pattern_error_for_missing_digits(self):
        self.assertRaises(InvalidCnpjPatternError,
                          parse_customer,
                          '002ç123123123123çDale CarnegieçFarming')

    def test_raise_invalid_cnpj_pattern_error_for_extra_digits(self):
        self.assertRaises(InvalidCnpjPatternError,
                          parse_customer,
                          '002ç123123123123120çDale CarnegieçFarming')
