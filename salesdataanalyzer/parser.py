import re

from salesdataanalyzer.helpers import Salesman
from salesdataanalyzer.settings import FIELD_SEPARATOR, ID_PATTERN, \
    CPF_PATTERN, SALARY_PATTERN


def parse_line_id(line: str) -> str:
    """Parses the data type identifier of the line and returns it.
    The id is the string that starts at the first character and ends at
    the character before the separator character. If the line doesn't
    contain any separator, the identifier is considered the entire line.
    Valid ids must match the pattern from ID_PATTERN in the settings
    file. If the id is invalid, raises InvalidIdPatternError.
    """
    sep_index = line.find(FIELD_SEPARATOR)

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
        _, cpf, name, salary = line.split(FIELD_SEPARATOR)
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
