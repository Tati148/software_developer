class Book:
    """Базовый класс книги. Хранит общее: название и автора."""
    def __init__(self, name: str, author: str):
        # «Скрываем» внутренние атрибуты для использования их через property
        self._name = name
        self._author = author

    @property
    def name(self):
        """Свойство только для чтения — название книги."""
        return self._name

    @property
    def author(self):
        """Свойство только для чтения — автор книги."""
        return self._author

    def __str__(self):
        """Строковое представление книги (print(book))."""
        return f"Книга «{self.name}». Автор: {self.author}"

    def __repr__(self):
        """
        Репрезентативное представление (например, при выводе списка объектов).
        Позволяет воссоздать аналогичный объект.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц (pages) должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц (pages) должно быть положительным.")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга «{self.name}». Автор: {self.author}. Страниц: {self.pages}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"
        )


class AudioBook(Book):
    """Класс аудиокниги, наследуется от Book и добавляет длительность."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # опять же через setter

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Длительность (duration) должна быть числом (float).")
        if value <= 0:
            raise ValueError("Длительность (duration) должна быть положительной.")
        self._duration = float(value)

    def __str__(self):
        """Расширяем строковое представление, добавляя длительность."""
        return f"Аудиокнига «{self.name}». Автор: {self.author}. Длительность: {self.duration}"

    def __repr__(self):
        """
        Отражаем новый атрибут (duration) в repr, чтобы объект можно было
        восстановить по этой строке.
        """
        return (
            f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
        )
