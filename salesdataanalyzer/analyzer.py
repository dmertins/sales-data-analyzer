from typing import List

from salesdataanalyzer.helpers import Data, DataSummary, Customer, Salesman


def analyze_data(data: Data) -> DataSummary:
    """Returns a summary of the analyzed input data."""


def count_customers(customers: List[Customer]) -> int:
    """Returns the quantity of customers."""
    return len(customers)


def count_salesmen(salesmen: List[Salesman]) -> int:
    """Returns the quantity of salesmen."""
    return len(salesmen)
