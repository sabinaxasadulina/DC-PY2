class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """

        :param name: Название книги
        :param author: Имя и фамилия автора

        Примеры:
        >>> Book(name="Гарри Поттер и философский камень", author='Дж.К.Роулинг')
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Бумажная книга """
    def __init__(self, name: str, author: str, pages: int):
        """

        :param name: Название книги
        :param author: Имя и фамилия автора
        :param pages: Количество страниц

        Примеры:
        >>> PaperBook(name="Гарри Поттер и философский камень", author='Дж.К.Роулинг', pages=300)
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """"Возвращает количество страниц книги"""
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            return TypeError(f"Не тот тип данных. Ожидается int, а не {type(pages)}")
        if not pages > 0:
            return ValueError("Количество страниц должно быть больше 0")
        self._pages = pages

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.pages!r})'

class AudioBook(Book):
    """ Электронная книга """
    def __init__(self, name: str, author: str, duration: float):
        """

        :param name: Название книги
        :param author: Имя и фамилия автора
        :param duration: Продолжительность аудиокниги

        Примеры:
        >>> AudioBook(name="Гарри Поттер и философский камень", author='Дж.К.Роулинг', duration=660)
        """
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """"Возвращает продолжительность книги"""
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            return TypeError(f"Не тот тип данных. Ожидается int, а не {type(duration)}")
        if not duration > 0:
            return ValueError("Продолжительность должна быть больше 0 минут")
        self._duration = duration

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration} минут"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.author}, {self.duration!r})'


