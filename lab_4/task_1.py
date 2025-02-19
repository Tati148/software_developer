class Animal:
    """
    Базовый класс для животных.

    Атрибуты:
        species (str): Вид животного (например, 'Dog', 'Cat', 'Tiger').
        habitat (str): Среда обитания (например, 'Forest', 'Domestic').
        _health (int): Скрытый (непубличный) атрибут, отражающий здоровье животного.
                       Инкапсулируем, чтобы не давать прямой доступ пользователю и
                       избежать некорректных изменений здоровья.
    """

    def __init__(self, species: str, habitat: str, health: int = 100):
        """
        Параметры:
            species (str): Вид животного.
            habitat (str): Среда обитания.
            health (int, необязательный): Показатель здоровья (по умолчанию 100).
        """
        self.species = species
        self.habitat = habitat
        self._health = health  # защищённый атрибут

    def make_sound(self) -> None:
        """
        Базовый метод издания звука.
        """
        print("Generic animal sound")

    def move(self) -> None:
        """
        Демонстрация передвижения животного.
        Может быть унаследован или переопределён в дочерних классах при необходимости.
        """
        print(f"The {self.species} moves around in a {self.habitat} environment.")

    def __str__(self) -> str:
        return f"{self.species} in {self.habitat} (health: {self._health})"

    def __repr__(self) -> str:
        return (f"Animal(species={self.species!r}, "
                f"habitat={self.habitat!r}, "
                f"health={self._health!r})")


class Cat(Animal):
    """
    Дочерний класс, представляющий кота.
    """

    def __init__(self, breed: str, health: int = 100):
        """
        Инициализирует кота.
        Устанавливает вид (species) = 'Cat' и среду обитания (habitat) = 'Domestic' по умолчанию.

        Параметры:
            breed (str): Порода кота
            health (int, необязательный): Показатель здоровья (100).
        """
        super().__init__(species="Cat", habitat="Domestic", health=health)
        self.breed = breed

    def make_sound(self) -> None:
        """
        Переопределяем базовый метод издания звука
        """
        print("Meow!")

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}. It's a {self.breed} cat."


if __name__ == "__main__":
    # Пример использования
    generic_animal = Animal(species="Unknown", habitat="Everywhere")
    print(generic_animal)
    print(repr(generic_animal))
    generic_animal.make_sound()
    generic_animal.move()

    print("—" * 40)

    siamese_cat = Cat(breed="Siamese", health=95)
    print(siamese_cat)
    print(repr(siamese_cat))
    siamese_cat.make_sound()
    siamese_cat.move()
