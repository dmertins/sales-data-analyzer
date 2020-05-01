import re

from salesdataanalyzer.settings import FIELD_SEPARATOR, ID_PATTERN


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
