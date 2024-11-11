# library_manager/utils/data_validation.py

def validate_book_data(data):
    required_fields = ['title', 'author', 'genre']
    for field in required_fields:
        if field not in data or not isinstance(data[field], str):
            return False
    return True
