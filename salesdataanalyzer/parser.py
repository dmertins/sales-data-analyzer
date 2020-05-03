import re
from typing import List

from salesdataanalyzer.helpers import Salesman, Customer, SaleItem
from salesdataanalyzer.settings import DATA_FIELD_SEPARATOR, ID_PATTERN, \
    CPF_PATTERN, SALARY_PATTERN, CNPJ_PATTERN, ITEM_ID_PATTERN, \
    QUANTITY_PATTERN, PRICE_PATTERN, ITEM_FIELD_SEPARATOR, \
    ITEM_LIST_START_DELIMITER, ITEM_LIST_END_DELIMITER, ITEM_LIST_SEPARATOR


def parse_line_id(line: str) -> str:
    """Parses the data type identifier of the line and returns it.
    The id is the string that starts at the first character and ends at
    the character before the separator character. If the line doesn't
    contain any separator, the identifier is considered the entire line.
    Valid ids must match the pattern from ID_PATTERN in the settings
    file. If the id is invalid, raises InvalidIdPatternError.
    """
    sep_index = line.find(DATA_FIELD_SEPARATOR)

    line_id = line[:sep_index] if sep_index != -1 else line

    if re.fullmatch(ID_PATTERN, line_id) is None:
        raise InvalidIdPatternError(line_id)

    return line_id


class InvalidIdPatternError(ValueError):
    pass


def parse_salesman(line: str) -> Salesman:
    """Parses line containing Salesman data type fields and returns a
    Salesman object. Raises InvalidNumberOfFieldsError if line string
    argument contains a number of fields different than expected for the
    Salesman object.
    Validated fields:
    cpf: raises InvalidCpfPatternError
    salary: raises InvalidSalaryPatternError
    """
    try:
        _, cpf, name, salary = line.split(DATA_FIELD_SEPARATOR)
    except ValueError:
        raise WrongNumberOfFieldsError(f'"{line}" (expected'
                                       f'"001ç<cpf>ç<name>ç<salary>")')

    if re.fullmatch(CPF_PATTERN, cpf) is None:
        raise InvalidCpfPatternError(f'"{cpf}" (expected 11-wide digit only)')

    if re.fullmatch(SALARY_PATTERN, salary) is None:
        raise InvalidSalaryPatternError(f'"{salary}"'
                                        f'(expected int or float pattern)')

    return Salesman(cpf, name, float(salary))


class WrongNumberOfFieldsError(ValueError):
    pass


class InvalidCpfPatternError(ValueError):
    pass


class InvalidSalaryPatternError(ValueError):
    pass


def parse_customer(line: str) -> Customer:
    """Parses line containing Customer data type fields and returns a
    Customer object. Raises InvalidNumberOfFieldsError if line string
    argument contains a number of fields different than expected for the
    Customer object.
    Validated fields:
    cnpj: raises InvalidCnpjPatternError
    """
    try:
        _, cnpj, name, business_area = line.split(DATA_FIELD_SEPARATOR)
    except ValueError:
        raise WrongNumberOfFieldsError(f'"{line}" (expected'
                                       f'"002ç<cnpj>ç<name>ç<business_area>")')

    if re.fullmatch(CNPJ_PATTERN, cnpj) is None:
        raise InvalidCnpjPatternError(f'"{cnpj}" '
                                      f'(expected 14-wide digit only)')

    return Customer(cnpj, name, business_area)


class InvalidCnpjPatternError(ValueError):
    pass


def parse_sale_item(item: str) -> SaleItem:
    """Parses a string containing raw sale item data and returns a
    SaleItem object. Raises WrongNumberOfFieldsError if the string
    contains a number of fields different than expected for the
    SaleItem object.
    Validated fields:
    item_id: raises InvalidItemIdPatternError
    quantity: raises InvalidQuantityPatternError
    price: raises InvalidPricePatternError
    """
    try:
        item_id, quantity, price = item.split(ITEM_FIELD_SEPARATOR)
    except ValueError:
        raise WrongNumberOfFieldsError(f'"{item}" (expected '
                                       f'"<item_id>-<quantity>-<price>")')

    if re.fullmatch(ITEM_ID_PATTERN, item_id) is None:
        raise InvalidItemIdPatternError(f'"{item_id}" (expected int)')

    if re.fullmatch(QUANTITY_PATTERN, quantity) is None:
        raise InvalidQuantityPatternError(f'"{quantity}" (expected int)')

    if re.fullmatch(PRICE_PATTERN, price) is None:
        raise InvalidPricePatternError(f'"{price}" (expected float)')

    return SaleItem(int(item_id), int(quantity), float(price))


class InvalidItemIdPatternError(ValueError):
    pass


class InvalidQuantityPatternError(ValueError):
    pass


class InvalidPricePatternError(ValueError):
    pass


def parse_sale_items_list(raw_items: str) -> List[SaleItem]:
    """Parses a string delimited by a start and end character,
    containing a list of Sale Items separated by a given character. The
    separator and the delimiter characters are defined in the settings
    file.
    Returns a list of SaleItem objects.
    Raises InvalidStartDelimiterError for invalid start delimiter.
    Raises InvalidEndDelimiterError for invalid end delimiter.
    """
    if not raw_items.startswith(ITEM_LIST_START_DELIMITER):
        raise InvalidStartDelimiterError(f'"{raw_items[0]}" in "{raw_items}" '
                                         f'(expected '
                                         f'"{ITEM_LIST_START_DELIMITER}")')

    if not raw_items.endswith(ITEM_LIST_END_DELIMITER):
        raise InvalidEndDelimiterError(f'"{raw_items[-1]}" in "{raw_items}" '
                                       f'(expected '
                                       f'"{ITEM_LIST_END_DELIMITER}")')

    raw_items = raw_items.lstrip(ITEM_LIST_START_DELIMITER)
    raw_items = raw_items.rstrip(ITEM_LIST_END_DELIMITER)

    raw_items_list = raw_items.split(ITEM_LIST_SEPARATOR)

    try:
        sale_items = [parse_sale_item(raw_item) for raw_item in raw_items_list]
    except (WrongNumberOfFieldsError, InvalidItemIdPatternError,
            InvalidQuantityPatternError, InvalidPricePatternError) as e:
        raise e

    return sale_items


class InvalidStartDelimiterError(ValueError):
    pass


class InvalidEndDelimiterError(ValueError):
    pass
