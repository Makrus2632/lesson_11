# library_manager/catalog.py

from library_manager.utils.data_validation import validate_book_data

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_data):
        if validate_book_data(book_data):
            self.books.append(book_data)
        else:
            raise ValueError("Invalid book data")

    def remove_book(self, title):
        self.books = [book for book in self.books if book.get('title') != title]

    def find_books(self, **criteria):
        results = self.books
        for key, value in criteria.items():
            results = [book for book in results if book.get(key) == value]
        return results

    def view_all_books(self):
        return self.books
