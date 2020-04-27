from typing import NamedTuple, List


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
