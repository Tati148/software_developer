import doctest


class Cup:
    def __init__(self, material: str, capacity: float):
        """
        Создание объекта "Чашка".

        :param material: Материал чашки (например, "керамика")
        :param capacity: Вместимость чашки в миллилитрах

        Примеры:
        >>> cup = Cup("керамика", 250.0)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not material.strip():
            raise ValueError("Материал не может быть пустым")
        self.material = material

        if not isinstance(capacity, (int, float)):
            raise TypeError("Объем должен быть числом")
        if capacity <= 0:
            raise ValueError("Объем должен быть положительным числом")
        self.capacity = capacity

        self.current_volume = 0.0

    def fill(self, amount: float) -> None:
        """
        Наполнить чашку жидкостью.

        :param amount: Количество жидкости в мл, которое нужно добавить
        :raise ValueError: Если количество жидкости отрицательное или превышает доступное место

        Примеры:
        >>> cup = Cup("керамика", 250.0)
        >>> cup.fill(100.0)
        >>> cup.current_volume
        100.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество жидкости должно быть числом")
        if amount < 0:
            raise ValueError("Количество жидкости не может быть отрицательным")
        if self.current_volume + amount > self.capacity:
            raise ValueError("Слишком много жидкости, чашка переполнится")
        self.current_volume += amount

    def empty(self) -> None:
        """
        Опустошить чашку.

        Примеры:
        >>> cup = Cup("керамика", 250.0)
        >>> cup.fill(100.0)
        >>> cup.empty()
        >>> cup.current_volume
        0.0
        """
        self.current_volume = 0.0

    def get_remaining_volume(self) -> float:
        """
        Узнать, сколько ещё жидкости можно добавить до заполнения.

        :return: Оставшееся свободное место в мл

        Примеры:
        >>> cup = Cup("керамика", 250.0)
        >>> cup.fill(100.0)
        >>> cup.get_remaining_volume()
        150.0
        """
        return self.capacity - self.current_volume


class Bag:
    def __init__(self, material: str, capacity_in_liters: float):
        """
        Создание объекта "Сумка".

        :param material: Материал сумки (например, "ткань")
        :param capacity_in_liters: Вместимость сумки в литрах

        Примеры:
        >>> bag = Bag("ткань", 10.0)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not material.strip():
            raise ValueError("Материал не может быть пустым")
        self.material = material

        if not isinstance(capacity_in_liters, (int, float)):
            raise TypeError("Вместимость сумки должна быть числом")
        if capacity_in_liters <= 0:
            raise ValueError("Вместимость должна быть положительным числом")
        self.capacity_in_liters = capacity_in_liters

        self.current_load = 0.0

    def put_item(self, volume: float) -> None:
        """
        Положить предмет в сумку.

        :param volume: Объём предмета в литрах
        :raise ValueError: Если предмет не помещается
        Примеры:
        >>> bag = Bag("кожа", 5.0)
        >>> bag.put_item(2.0)
        >>> bag.current_load
        2.0
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объём предмета должен быть числом")
        if volume <= 0:
            raise ValueError("Объём предмета должен быть положительным")
        if self.current_load + volume > self.capacity_in_liters:
            raise ValueError("Предмет не помещается в сумку")
        self.current_load += volume

    def remove_item(self, volume: float) -> None:
        """
        Извлечь предмет из сумки.

        :param volume: Объём предмета в литрах
        :raise ValueError: Если в сумке нет такого количества для извлечения
        Примеры:
        >>> bag = Bag("ткань", 3.0)
        >>> bag.put_item(1.0)
        >>> bag.remove_item(1.0)
        >>> bag.current_load
        0.0
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объём предмета должен быть числом")
        if volume <= 0:
            raise ValueError("Объём предмета должен быть положительным")
        if volume > self.current_load:
            raise ValueError("В сумке нет такого объёма для извлечения")
        self.current_load -= volume

    def check_free_space(self) -> float:
        """
        Проверить, сколько свободного места осталось в сумке.

        :return: Свободное место в литрах

        Примеры:
        >>> bag = Bag("ткань", 3.0)
        >>> bag.check_free_space()
        3.0
        """
        return self.capacity_in_liters - self.current_load


class Pen:
    def __init__(self, color: str, ink_level: float):
        """
        Создание объекта "Ручка".

        :param color: Цвет чернил
        :param ink_level: Количество чернил (мл) в ручке

        Примеры:
        >>> pen = Pen("синий", 1.0)
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        if not color.strip():
            raise ValueError("Цвет не может быть пустым")
        self.color = color

        if not isinstance(ink_level, (int, float)):
            raise TypeError("Количество чернил должно быть числом")
        if ink_level < 0:
            raise ValueError("Количество чернил не может быть отрицательным")
        self.ink_level = ink_level

    def write(self, char_count: int) -> None:
        """
        Писать ручкой заданное количество символов.
        Предположим, что для написания одного символа тратится 0.01 мл чернил.

        :param char_count: Количество символов для написания
        :raise ValueError: Если символов отрицательное число или не хватает чернил

        Примеры:
        >>> pen = Pen("чёрный", 1.0)
        >>> pen.write(10)
        >>> pen.ink_level
        0.9
        """
        if not isinstance(char_count, int):
            raise TypeError("Количество символов должно быть целым числом")
        if char_count < 0:
            raise ValueError("Количество символов не может быть отрицательным")

        ink_needed = char_count * 0.01
        if ink_needed > self.ink_level:
            raise ValueError("Недостаточно чернил для написания такого количества символов")

        self.ink_level -= ink_needed

    def refill(self, amount: float) -> None:
        """
        Пополнить чернила в ручке.

        :param amount: Количество добавляемых чернил (мл)
        :raise ValueError: Если количество добавляемых чернил отрицательно

        Примеры:
        >>> pen = Pen("синий", 0.5)
        >>> pen.refill(0.5)
        >>> pen.ink_level
        1.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество чернил должно быть числом")
        if amount < 0:
            raise ValueError("Количество чернил не может быть отрицательным")
        self.ink_level += amount

    def check_ink(self) -> float:
        """
        Проверить оставшееся количество чернил.

        :return: Текущее количество чернил (мл)

        Примеры:
        >>> pen = Pen("синий", 1.0)
        >>> pen.check_ink()
        1.0
        """
        return self.ink_level


if __name__ == "__main__":
    doctest.testmod()