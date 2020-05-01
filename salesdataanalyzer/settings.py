from pathlib import Path

INPUT_DIR_PATH = Path.home() / 'data' / 'in'
OUTPUT_DIR_PATH = Path.home() / 'data' / 'out'

INPUT_FILE_EXT = '.dat'
REPORT_FILE_EXT = '.done.dat'

REPORT_TEMPLATE = 'customers amount: {customers_amount}\n'\
                  'salesmen amount: {salesmen_amount}\n' \
                  'most expensive sale id: {most_expensive_sale_id}\n' \
                  'worst salesman name: {worst_salesman_name}'

FIELD_SEPARATOR = 'ç'
