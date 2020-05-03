from unittest import TestCase

from salesdataanalyzer.helpers import Salesman
from salesdataanalyzer.parser import parse_salesman,\
    WrongNumberOfFieldsError, InvalidCpfPatternError, InvalidSalaryPatternError


class ParseSalesmanTest(TestCase):
    def test_parse_salesman(self):
        salesman = parse_salesman('001ç12312312312çJohn H. Pattersonç'
                                  '192000.00')

        self.assertEqual(Salesman('12312312312',
                                  'John H. Patterson',
                                  192000.00),
                         salesman)

    def test_raise_wrong_number_of_fields_error_for_missing_field(self):
        self.assertRaises(WrongNumberOfFieldsError,
                          parse_salesman,
                          '001ç12312312312çJohn H. Patterson')

    def test_raise_wrong_number_of_fields_error_for_extra_field(self):
        self.assertRaises(WrongNumberOfFieldsError,
                          parse_salesman,
                          '001ç12312312312çJohn H. Pattersonç'
                          '192000.00çExtra Field')

    def test_raise_invalid_cpf_pattern_error_for_invalid_characters(self):
        self.assertRaises(InvalidCpfPatternError,
                          parse_salesman,
                          '001ç123abc12312çJohn H. Pattersonç192000.00')

    def test_raise_invalid_cpf_pattern_error_for_missing_digits(self):
        self.assertRaises(InvalidCpfPatternError,
                          parse_salesman,
                          '001ç123123123çJohn H. Pattersonç192000.00')

    def test_raise_invalid_cpf_pattern_error_for_extra_digits(self):
        self.assertRaises(InvalidCpfPatternError,
                          parse_salesman,
                          '001ç123123123120çJohn H. Pattersonç192000.00')

    def test_raise_invalid_salary_pattern_error_for_invalid_character(self):
        self.assertRaises(InvalidSalaryPatternError,
                          parse_salesman,
                          '001ç12312312312çJohn H. Pattersonç192,000.00')

    def test_raise_invalid_salary_pattern_error_for_empty_field(self):
        self.assertRaises(InvalidSalaryPatternError,
                          parse_salesman,
                          '001ç12312312312çJohn H. Pattersonç')
