from unittest import TestCase

from salesdataanalyzer.analyzer import count_customers
from salesdataanalyzer.helpers import Customer


class CountCustomersTest(TestCase):
    def test_count_customers(self):
        customers_amount = count_customers([
            Customer('12312312312312', 'Dale Carnegie', 'Farming'),
            Customer('45645645645645', 'Joe Girard', 'Automotive Retail'),
        ])

        self.assertEqual(2, customers_amount)

    def test_count_customers_for_empty_list(self):
        customers_amount = count_customers([])

        self.assertEqual(0, customers_amount)
