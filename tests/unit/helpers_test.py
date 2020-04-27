from unittest import TestCase

from salesdataanalyzer.helpers import Salesman, Customer


class SalesmanTest(TestCase):
    def test_create_salesman(self):
        salesman = Salesman('12312312312', 'John H. Patterson', 192000.00)

        self.assertEqual('12312312312', salesman.cpf)
        self.assertEqual('John H. Patterson', salesman.name)
        self.assertEqual(192000.00, salesman.salary)


class CustomerTest(TestCase):
    def test_create_customer(self):
        customer = Customer('12312312312312', 'Dale Carnegie', 'Farming')

        self.assertEqual('12312312312312', customer.cnpj)
        self.assertEqual('Dale Carnegie', customer.name)
        self.assertEqual('Farming', customer.business_area)
