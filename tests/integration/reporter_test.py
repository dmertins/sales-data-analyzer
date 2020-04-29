import os
from unittest import TestCase

from salesdataanalyzer import reporter
from salesdataanalyzer.reporter import MissingDataSummaryKeyError, \
    FileNameContainsDirPathError, FileNameTooLongError
from salesdataanalyzer.settings import OUTPUT_DIR_PATH, REPORT_FILE_EXT, \
    REPORT_TEMPLATE
from tests.helper import wait_for

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

        wait_for(lambda: self.assertTrue(REPORT_FILE_PATH.exists(),
                                         "Report file wasn't created"))

        with REPORT_FILE_PATH.open(mode='r', encoding='utf-8') as report_file:
            report_text = report_file.read()

        self.assertEqual(EXPECTED_REPORT_TEXT, report_text)

    def test_raise_missing_data_summary_field_error(self):
        self.assertRaises(MissingDataSummaryKeyError,
                          reporter.write_report_file,
                          FILE_NAME,
                          {
                              'customers_amount': 3,
                              'salesmen_amount': 3,
                              'most_expensive_sale_id': 6,
                          })

    def test_raise_file_name_contains_dir_path_error(self):
        self.assertRaises(FileNameContainsDirPathError,
                          reporter.write_report_file,
                          'dir' + os.path.sep + 'file_name',
                          DATA_SUMMARY)

    def test_raise_file_name_too_long_error(self):
        self.assertRaises(FileNameTooLongError,
                          reporter.write_report_file,
                          'a' * (255 - len(REPORT_FILE_EXT) + 1),
                          DATA_SUMMARY)
