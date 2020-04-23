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

    report_file_path = OUTPUT_DIR_PATH / (file_name + REPORT_FILE_EXT)
    report_file_path.parent.mkdir(parents=True, exist_ok=True)
    with report_file_path.open(mode='w', encoding='utf-8') as report_file:
        report_file.write(report_text)


class MissingDataSummaryKeyError(KeyError):
    pass
