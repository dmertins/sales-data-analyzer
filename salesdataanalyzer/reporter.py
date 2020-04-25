import os
from typing import TypedDict

from salesdataanalyzer.settings import OUTPUT_DIR_PATH, REPORT_FILE_EXT, \
    REPORT_TEMPLATE


class DataSummary(TypedDict):
    customers_amount: int
    salesmen_amount: int
    most_expensive_sale_id: int
    worst_salesman_name: str


def write_report_file(file_name: str, data_summary: DataSummary) -> None:
    """Writes a report file in the output directory."""
    try:
        report_text = REPORT_TEMPLATE.format(
            customers_amount=data_summary['customers_amount'],
            salesmen_amount=data_summary['salesmen_amount'],
            most_expensive_sale_id=data_summary['most_expensive_sale_id'],
            worst_salesman_name=data_summary['worst_salesman_name']
        )
    except KeyError as e:
        raise MissingDataSummaryKeyError(f'{e.args[0]} in {data_summary}')

    if contains_dir_path(file_name):
        raise FileNameContainsDirPathError(file_name)

    if is_too_long(file_name):
        raise FileNameTooLongError(file_name)

    report_file_path = OUTPUT_DIR_PATH / (file_name + REPORT_FILE_EXT)
    report_file_path.parent.mkdir(parents=True, exist_ok=True)

    with report_file_path.open(mode='w', encoding='utf-8') as report_file:
        report_file.write(report_text)


def contains_dir_path(file_name: str) -> bool:
    """Returns True if file_name contains OS path components separator.
    Returns False otherwise."""
    return os.path.sep in file_name


def is_too_long(file_name: str) -> bool:
    """Returns True if file_name concatenated with file extension
    length is > 255. Returns False otherwise."""
    return len(file_name + REPORT_FILE_EXT) > 255


class MissingDataSummaryKeyError(KeyError):
    pass


class FileNameContainsDirPathError(ValueError):
    pass


class FileNameTooLongError(OSError):
    pass
