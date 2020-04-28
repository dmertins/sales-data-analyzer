from unittest import TestCase, skip

from salesdataanalyzer.analyzer import analyze_data
from salesdataanalyzer.helpers import Salesman, Customer, Sale, SaleItem, \
    DataSummary


class AnalyzerTest(TestCase):
    @skip
    def test_analyze_data(self):
        salesmen = [
            Salesman('12312312312', 'John H. Patterson', 192000.00),
            Salesman('45645645645', 'David Ogilvy', 167500.00),
        ]

        customers = [
            Customer('12312312312312', 'Dale Carnegie', 'Farming'),
            Customer('45645645645645', 'Joe Girard', 'Automotive Retail'),
        ]

        sales = [
            Sale(1, [SaleItem(1, 1, 110500.99)], 'John H. Patterson'),
            Sale(2, [SaleItem(2, 25, 230.45)], 'David Ogilvy'),
            Sale(4, [SaleItem(4, 1, 65198.90)], 'John H. Patterson'),
            Sale(5, [SaleItem(5, 5, 470.10)], 'David Ogilvy'),
        ]

        data_summary: DataSummary = analyze_data({
                                                     'salesmen': salesmen,
                                                     'customers': customers,
                                                     'sales': sales,
                                                 })

        expected_data_summary: DataSummary = {
            'customers_amount': 2,
            'salesmen_amount': 2,
            'most_expensive_sale_id': 1,
            'worst_salesman_name': 'David Ogilvy',
        }

        self.assertDictEqual(expected_data_summary, data_summary)
