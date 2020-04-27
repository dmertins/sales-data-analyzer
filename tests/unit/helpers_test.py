from unittest import TestCase

from salesdataanalyzer.helpers import Salesman


class SalesmanTest(TestCase):
    def test_create_salesman(self):
        salesman = Salesman('12312312312', 'John H. Patterson', 192000.00)

        self.assertEqual('12312312312', salesman.cpf)
        self.assertEqual('John H. Patterson', salesman.name)
        self.assertEqual(192000.00, salesman.salary)
