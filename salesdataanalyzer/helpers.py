from typing import NamedTuple, List, TypedDict


class Salesman(NamedTuple):
    cpf: str
    name: str
    salary: float


class Customer(NamedTuple):
    cnpj: str
    name: str
    business_area: str


class SaleItem(NamedTuple):
    item_id: int
    quantity: int
    price: float


class Sale(NamedTuple):
    sale_id: int
    items: List[SaleItem]
    salesman_name: str


class Data(TypedDict):
    salesmen: List[Salesman]
    customers: List[Customer]
    sales: List[Sale]


class DataSummary(TypedDict):
    customers_amount: int
    salesmen_amount: int
    most_expensive_sale_id: int
    worst_salesman_name: str
