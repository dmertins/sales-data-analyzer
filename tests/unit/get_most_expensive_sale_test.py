from unittest import TestCase

from salesdataanalyzer.analyzer import get_most_expensive_sale
from salesdataanalyzer.helpers import Sale, SaleItem


class GetMostExpensiveSaleTest(TestCase):
    def test_get_most_expensive_sale(self):
        sale = get_most_expensive_sale([
            Sale(1, [SaleItem(1, 1, 110500.99)], 'John H. Patterson'),
            Sale(2, [SaleItem(2, 25, 230.45)], 'David Ogilvy'),
        ])

        self.assertEqual(1, sale.sale_id)
        self.assertEqual(1, sale.items[0].item_id)
        self.assertEqual(1, sale.items[0].quantity)
        self.assertEqual(110500.99, sale.items[0].price)
        self.assertEqual('John H. Patterson', sale.salesman_name)

    def test_get_most_expensive_sale_for_empty_list(self):
        sale = get_most_expensive_sale([])

        self.assertEqual(None, sale)
