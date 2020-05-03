from pathlib import Path

INPUT_DIR_PATH = Path.home() / 'data' / 'in'
OUTPUT_DIR_PATH = Path.home() / 'data' / 'out'

INPUT_FILE_EXT = '.dat'
REPORT_FILE_EXT = '.done.dat'

REPORT_TEMPLATE = 'customers amount: {customers_amount}\n'\
                  'salesmen amount: {salesmen_amount}\n' \
                  'most expensive sale id: {most_expensive_sale_id}\n' \
                  'worst salesman name: {worst_salesman_name}'

DATA_FIELD_SEPARATOR = 'ç'
ID_PATTERN = '[0-9]+'

CPF_PATTERN = '[0-9]{11}'
SALARY_PATTERN = '[0-9]+.?[0-9]*'

CNPJ_PATTERN = '[0-9]{14}'

ITEM_FIELD_SEPARATOR = '-'
ITEM_ID_PATTERN = '[0-9]+'
QUANTITY_PATTERN = '[0-9]+'
PRICE_PATTERN = '[0-9]+.?[0-9]*'

ITEM_LIST_START_DELIMITER = '['
ITEM_LIST_END_DELIMITER = ']'
ITEM_LIST_SEPARATOR = ','

SALE_ID_PATTERN = '[0-9]+'
