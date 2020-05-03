from unittest import TestCase

from salesdataanalyzer.helpers import Sale, SaleItem
from salesdataanalyzer.parser import parse_sale, WrongNumberOfFieldsError, \
    InvalidSaleIdPatternError


class ParseSaleTest(TestCase):
    def test_parse_sale(self):
        sale = parse_sale('003ç001ç[01-1-110500.99]çJohn H. Patterson')

        self.assertEqual(Sale(1,
                              [SaleItem(1, 1, 110500.99)],
                              'John H. Patterson'),
                         sale)

    def test_raise_wrong_number_of_fields_error_for_missing_field(self):
        self.assertRaises(WrongNumberOfFieldsError,
                          parse_sale,
                          '003ç001ç[01-1-110500.99]')

    def test_raise_wrong_number_of_fields_error_for_extra_field(self):
        self.assertRaises(WrongNumberOfFieldsError,
                          parse_sale,
                          '003ç001ç[01-1-110500.99]çJohn H. Pattersonç'
                          'Extra Field')

    def test_raise_invalid_sale_id_pattern_error(self):
        self.assertRaises(InvalidSaleIdPatternError,
                          parse_sale,
                          '003çid_001ç[01-1-110500.99]çJohn H. Patterson')
