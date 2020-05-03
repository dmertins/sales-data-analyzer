from unittest import TestCase

from salesdataanalyzer.parser import parse_line_id, InvalidIdPatternError


class ParseLineIdTest(TestCase):
    def test_parse_line_valid_id(self):
        line_id = parse_line_id('001ç12312312312çJohn H. Pattersonç192000.00')

        self.assertEqual('001', line_id,
                         'parsed id should be {}'.format('001'))

    def test_parse_line_invalid_id(self):
        self.assertRaises(InvalidIdPatternError,
                          parse_line_id,
                          'id_001ç45645645645çDavid Ogilvyç167500.00')

    def test_parse_line_valid_id_without_separator(self):
        line_id = parse_line_id('000002')

        self.assertEqual('000002', line_id,
                         'parsed id should be {}'.format('000002'))

    def test_parse_line_invalid_id_without_separator(self):
        self.assertRaises(InvalidIdPatternError,
                          parse_line_id,
                          'id_000002')
