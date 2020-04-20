import time
from unittest import TestCase

from salesdataanalyzer import reporter
from salesdataanalyzer.settings import OUTPUT_DIR_PATH, REPORT_FILE_EXT, \
    REPORT_TEMPLATE

MAX_WAIT = 0.5

FILE_NAME = 'test_data'
REPORT_FILE_PATH = OUTPUT_DIR_PATH / (FILE_NAME + REPORT_FILE_EXT)

DATA_SUMMARY = {
    'customers_amount': 3,
    'salesmen_amount': 3,
    'most_expensive_sale_id': 6,
    'worst_salesman_name': 'David Ogilvy',
}

EXPECTED_REPORT_TEXT = REPORT_TEMPLATE.format(
    customers_amount=DATA_SUMMARY['customers_amount'],
    salesmen_amount=DATA_SUMMARY['salesmen_amount'],
    most_expensive_sale_id=DATA_SUMMARY['most_expensive_sale_id'],
    worst_salesman_name=DATA_SUMMARY['worst_salesman_name']
)


class WriteReportFileTest(TestCase):
    def tearDown(self):
        REPORT_FILE_PATH.unlink(missing_ok=True)

    def test_write_report_file(self):
        reporter.write_report_file(FILE_NAME, DATA_SUMMARY)

        self.wait_for_report_file_to_be_created(REPORT_FILE_PATH)

        with REPORT_FILE_PATH.open(mode='r', encoding='utf-8') as report_file:
            report_text = report_file.read()

        self.assertEqual(EXPECTED_REPORT_TEXT, report_text)

    def wait_for_report_file_to_be_created(self, file_path):
        start_time = time.time()
        while True:
            try:
                self.assertTrue(file_path.exists(),
                                "Report file wasn't created")
                return
            except AssertionError as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.025)
