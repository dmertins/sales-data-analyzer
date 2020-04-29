from typing import List, Optional

from salesdataanalyzer.helpers import Data, DataSummary, Customer, Salesman, \
    Sale


def analyze_data(data: Data) -> DataSummary:
    """Returns a summary of the analyzed input data."""
    most_expensive_sale = get_most_expensive_sale(data['sales'])
    worst_salesman = get_worst_salesman(data['salesmen'], data['sales'])

    return {
        'customers_amount': count_customers(data['customers']),
        'salesmen_amount': count_salesmen(data['salesmen']),
        'most_expensive_sale_id': most_expensive_sale.sale_id,
        'worst_salesman_name': worst_salesman.name,
    }


def count_customers(customers: List[Customer]) -> int:
    """Returns the quantity of customers."""
    return len(customers)


def count_salesmen(salesmen: List[Salesman]) -> int:
    """Returns the quantity of salesmen."""
    return len(salesmen)


def get_most_expensive_sale(sales: List[Sale]) -> Optional[Sale]:
    """Returns the most expensive sale."""
    most_expensive_sale = None
    max_sale_total = 0

    for sale in sales:
        sale_total = 0

        for sale_item in sale.items:
            sale_total += sale_item.quantity * sale_item.price

        if sale_total > max_sale_total:
            max_sale_total = sale_total
            most_expensive_sale = sale

    return most_expensive_sale


def get_worst_salesman(salesmen: List[Salesman],
                       sales: List[Sale]) -> Optional[Salesman]:
    """Returns the worst salesman."""
    salesmen_total_values = {salesman.name: 0 for salesman in salesmen}

    for sale in sales:
        sale_total = 0

        for sale_item in sale.items:
            sale_total += sale_item.quantity * sale_item.price

        salesmen_total_values[sale.salesman_name] = salesmen_total_values.get(
            sale.salesman_name, 0) + sale_total

    if not salesmen_total_values:
        return None

    worst_salesman_name = min(salesmen_total_values,
                              key=salesmen_total_values.get)

    for salesman in salesmen:
        if salesman.name == worst_salesman_name:
            return salesman
