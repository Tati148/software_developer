BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """
        Конструктор принимает необязательный параметр books.
        Если он не передан, по умолчанию список книг будет пустым.
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги:
        - 1, если библиотека пока пуста,
        - иначе id последней книги + 1.
        """
        if not self.books:  # если список книг пуст
            return 1
        # Если есть хотя бы одна книга, ориентируемся на последнюю в списке
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке self.books по переданному book_id.
        Если книги с таким id нет, выбрасывает ValueError.
        """
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    # Пример 1: создаём пустую библиотеку
    empty_library = Library()
    print(empty_library.get_next_book_id()) # Вернётся 1, так как книг нет

    # Пример 2: инициализируем библиотеку списком книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)

    # Проверяем следующий id для библиотеки, где уже есть книги
    print(library_with_books.get_next_book_id())  # должно быть 3, если последняя книга с id=2

    # Проверяем метод get_index_by_book_id
    print(
        library_with_books.get_index_by_book_id(1))  # вернёт индекс книги с id=1
