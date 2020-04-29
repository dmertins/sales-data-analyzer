from unittest import TestCase

from salesdataanalyzer.analyzer import get_worst_salesman
from salesdataanalyzer.helpers import Sale, SaleItem, Salesman


class GetWorstSalesmanTest(TestCase):
    def test_get_worst_salesman(self):
        salesman = get_worst_salesman([
                                          Salesman('12312312312',
                                                   'John H. Patterson',
                                                   192000.00),
                                          Salesman('45645645645',
                                                   'David Ogilvy', 167500.00),
                                      ],
                                      [
                                            Sale(1,
                                                 [SaleItem(1, 1, 110500.99)],
                                                 'John H. Patterson'),
                                            Sale(2,
                                                 [SaleItem(2, 25, 230.45)],
                                                 'David Ogilvy'),
                                      ],
                                      )

        self.assertEqual(Salesman('45645645645', 'David Ogilvy', 167500.00),
                         salesman)

    def test_get_salesman_without_sales(self):
        salesman = get_worst_salesman([
                                          Salesman('12312312312',
                                                   'John H. Patterson',
                                                   192000.00),
                                          Salesman('45645645645',
                                                   'David Ogilvy', 167500.00),
                                      ],
                                      [
                                            Sale(1,
                                                 [SaleItem(1, 1, 110500.99)],
                                                 'John H. Patterson'),
                                      ],
                                      )

        self.assertEqual(Salesman('45645645645', 'David Ogilvy', 167500.00),
                         salesman)

    def test_get_none_for_empty_salesmen_list(self):
        salesman = get_worst_salesman([], [])

        self.assertEqual(None, salesman)