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
        # метод, отвечающий за строковое представление (print(book))
        return f'Книга "{self.name}"'

    def __repr__(self):
        # метод, возвращающий конструкцию, с помощью которой можно создать такой же объект
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    # проверяем метод __str__ (вывод строкового представления объектов)
    for book in list_books:
        print(book)

    # проверяем метод __repr__ (список объектов в виде python-конструкторов)
    print(list_books)