# library_manager/report.py

from library_manager.utils.formatting import format_book_data

def generate_report(library):
    report = "Отчет о работе библиотеки:\n"
    for book in library.view_all_books():
        report += format_book_data(book) + "\n"
    return report
