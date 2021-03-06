from unittest import TestCase, skip

from salesdataanalyzer import app
from salesdataanalyzer.settings import INPUT_DIR_PATH, OUTPUT_DIR_PATH, \
    REPORT_TEMPLATE, REPORT_FILE_EXT, INPUT_FILE_EXT
from tests.helper import wait_for

DATA_LINES = [
    '001' 'ç' '12312312312' 'ç' 'John H. Patterson' 'ç' '192000.00' '\n',
    '001' 'ç' '45645645645' 'ç' 'David Ogilvy'      'ç' '167500.00' '\n',
    '001' 'ç' '78978978978' 'ç' 'Mary Kay Ash'      'ç' '125800.00' '\n',
    '002' 'ç' '12312312312312' 'ç' 'Dale Carnegie' 'ç' 'Farming'           '\n',
    '002' 'ç' '45645645645645' 'ç' 'Joe Girard'    'ç' 'Automotive Retail' '\n',
    '002' 'ç' '78978978978978' 'ç' 'Erica Feidner' 'ç' 'Music Industry'    '\n',
    '003' 'ç' '001' 'ç' '[01-1-110500.99]' 'ç' 'John H. Patterson' '\n',
    '003' 'ç' '002' 'ç' '[02-25-230.45]'   'ç' 'David Ogilvy'      '\n',
    '003' 'ç' '003' 'ç' '[03-100-49.90]'   'ç' 'Mary Kay Ash'      '\n',
    '003' 'ç' '004' 'ç' '[04-1-65198.90' ',' '007-2-7200.00]'  'ç' 'John H. Patterson' '\n',
    '003' 'ç' '005' 'ç' '[05-5-470.10'   ',' '008-12-370.25]'  'ç' 'David Ogilvy'      '\n',
    '003' 'ç' '006' 'ç' '[06-250-98.89'  ',' '009-1115-78,69]' 'ç' 'Mary Kay Ash'      '\n',
]

EXPECTED_REPORT_TEXT = REPORT_TEMPLATE.format(
    customers_amount=3, salesmen_amount=3, most_expensive_sale_id=6,
    worst_salesman_name='David Ogilvy'
)

FILE_NAME = 'test_data'
DATA_FILE_PATH = INPUT_DIR_PATH / (FILE_NAME + INPUT_FILE_EXT)
REPORT_FILE_PATH = OUTPUT_DIR_PATH / (FILE_NAME + REPORT_FILE_EXT)


class AppTest(TestCase):
    def setUp(self):
        DATA_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        DATA_FILE_PATH.unlink()
        REPORT_FILE_PATH.unlink(missing_ok=True)

    @skip
    def test_data_summary_in_report_file(self):
        with DATA_FILE_PATH.open(mode='w', encoding='utf-8') as data_file:
            data_file.writelines(DATA_LINES)

        app.main()

        wait_for(lambda: self.assertTrue(REPORT_FILE_PATH.exists(),
                                         "Report file wasn't created"))

        with REPORT_FILE_PATH.open(mode='r', encoding='utf-8') as report_file:
            report_text = report_file.read()

        self.assertEqual(EXPECTED_REPORT_TEXT, report_text)
