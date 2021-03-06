from unittest import TestCase

from salesdataanalyzer.helpers import Salesman, Customer, SaleItem, Sale


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


class SaleItemTest(TestCase):
    def test_create_sale_item(self):
        sale_item = SaleItem(1, 1, 110500.99)

        self.assertEqual(1, sale_item.item_id)
        self.assertEqual(1, sale_item.quantity)
        self.assertEqual(110500.99, sale_item.price)


class SaleTest(TestCase):
    def test_create_sale(self):
        sale_items = [SaleItem(1, 1, 110500.99), SaleItem(4, 1, 65198.90)]
        sale = Sale(1, sale_items, 'John H. Patterson')

        self.assertEqual(1, sale.sale_id)
        self.assertEqual(sale_items, sale.items)
        self.assertEqual('John H. Patterson', sale.salesman_name)
