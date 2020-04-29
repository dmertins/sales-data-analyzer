from unittest import TestCase

from salesdataanalyzer.analyzer import count_salesmen
from salesdataanalyzer.helpers import Salesman


class CountSalesmenTest(TestCase):
    def test_count_salesmen(self):
        salesmen_amount = count_salesmen([
            Salesman('12312312312', 'John H. Patterson', 192000.00),
            Salesman('45645645645', 'David Ogilvy', 167500.00),
        ])

        self.assertEqual(2, salesmen_amount)

    def test_count_salesmen_for_empty_list(self):
        salesmen_amount = count_salesmen([])

        self.assertEqual(0, salesmen_amount)
