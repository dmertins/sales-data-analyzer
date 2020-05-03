from unittest import TestCase

from salesdataanalyzer.helpers import SaleItem
from salesdataanalyzer.parser import parse_sale_items_list, \
    InvalidStartDelimiterError, InvalidEndDelimiterError


class ParseSaleItemsListTest(TestCase):
    def test_parse_sale_items_list(self):
        sale_items = parse_sale_items_list('[04-1-65198.90,07-2-7200.00]')

        self.assertEqual([SaleItem(4, 1, 65198.90), SaleItem(7, 2, 7200.00)],
                         sale_items)

    def test_raise_invalid_start_delimiter_error(self):
        self.assertRaises(InvalidStartDelimiterError,
                          parse_sale_items_list,
                          '{04-1-65198.90,07-2-7200.00]')

    def test_raise_invalid_end_delimiter_error(self):
        self.assertRaises(InvalidEndDelimiterError,
                          parse_sale_items_list,
                          '[04-1-65198.90,07-2-7200.00}')
