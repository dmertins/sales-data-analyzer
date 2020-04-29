from typing import List, Optional

from salesdataanalyzer.helpers import Data, DataSummary, Customer, Salesman, \
    Sale


def analyze_data(data: Data) -> DataSummary:
    """Returns a summary of the analyzed input data."""


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
