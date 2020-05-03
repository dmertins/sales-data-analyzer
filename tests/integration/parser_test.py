from unittest import TestCase

from salesdataanalyzer.helpers import Salesman, Customer, Sale, SaleItem
from salesdataanalyzer.parser import parse_data


class ParserTest(TestCase):
    def test_parse_data(self):
        data = parse_data([
            '001ç12312312312çJohn H. Pattersonç192000.00',
            '002ç12312312312312çDale CarnegieçFarming',
            '003ç001ç[01-1-110500.99]çJohn H. Patterson',
        ])

        self.assertEqual({
            'salesmen': [
                Salesman('12312312312', 'John H. Patterson', 192000.00),
            ],
            'customers': [
                Customer('12312312312312', 'Dale Carnegie', 'Farming'),
            ],
            'sales': [
                Sale(1, [SaleItem(1, 1, 110500.99)], 'John H. Patterson'),
            ],
        },
                         data)

    def test_parse_empty_data(self):
        data = parse_data([])

        self.assertEqual({'salesmen': [], 'customers': [], 'sales': []}, data)

    def test_parse_nonexistent_data_id(self):
        data = parse_data(['004ç12312312312çJohn H. Pattersonç192000.00'])

        self.assertEqual({'salesmen': [], 'customers': [], 'sales': []}, data)
