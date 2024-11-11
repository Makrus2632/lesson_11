from library_manager.catalog import Library
from library_manager.report import generate_report

# Создаем экземпляр библиотеки
library = Library()

# Добавляем книги в библиотеку
library.add_book({"title": "Python 101", "author": "Mike Driscoll", "genre": "Programming"})
library.add_book({"title": "Machine Learning Basics", "author": "John Smith", "genre": "Data Science"})

# Поиск книги по названию
search_results = library.find_books(title="Machine Learning Basics")
print("Search Results:", search_results)

# Генерация отчета о всех книгах
report = generate_report(library)
print(report)

