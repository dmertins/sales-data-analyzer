from unittest import TestCase

from salesdataanalyzer.helpers import SaleItem
from salesdataanalyzer.parser import parse_sale_item,\
    WrongNumberOfFieldsError, InvalidItemIdPatternError,\
    InvalidQuantityPatternError, InvalidPricePatternError


class ParseSaleItemTest(TestCase):
    def test_parse_sale_item(self):
        sale_item = parse_sale_item('01-1-110500.99')

        self.assertEqual(SaleItem(1, 1, 110500.99), sale_item)

    def test_raise_wrong_number_of_fields_error_for_missing_field(self):
        self.assertRaises(WrongNumberOfFieldsError,
                          parse_sale_item,
                          '01-1')

    def test_raise_wrong_number_of_fields_error_for_extra_field(self):
        self.assertRaises(WrongNumberOfFieldsError,
                          parse_sale_item,
                          '01-1-110500.99-Extra Field')

    def test_raise_invalid_item_id_pattern_error_for_invalid_characters(self):
        self.assertRaises(InvalidItemIdPatternError,
                          parse_sale_item,
                          'id_01-1-110500.99')

    def test_raise_invalid_quantity_pattern_error_for_invalid_characters(self):
        self.assertRaises(InvalidQuantityPatternError,
                          parse_sale_item,
                          '01-1.0-110500.99')

    def test_raise_invalid_price_pattern_error_for_invalid_characters(self):
        self.assertRaises(InvalidPricePatternError,
                          parse_sale_item,
                          '01-1-110,500.99')
