class VideoGame:
    """ Базовый класс игры """
    def __init__(self, title: str, release_date: str, developer: str):
        """
        Базовый класс видеоигры
        :param title: Название игры
        :param release_date: Дата выхода
        :param developer: Разработчик игры

        Примеры:
        >>> VideoGame("Cuphead", "29.09.2017", "Studio MDHR")
        """
        self._title = title # Непубличный параметр, так как данные статичны
        self._release_date = release_date # Непубличный параметр, так как данные статичны
        self._developer = developer # Непубличный параметр, так как данные статичны
        self.review_grade = None # Параметр добавляется посредством метода add_review_grade, по умолчанию отсутствует

    @property
    def title(self):
        """
        Геттер для параметра Название игры
        """
        return self._title

    @property
    def developer(self):
        """
        Геттер для параметра Разработчик игры
        """
        return self._developer

    @property
    def release_date(self):
        """
        Геттер для параметра Дата выхода
        """
        return self._release_date

    def add_review_grade(self, rating: int):
        """
        Метод позволяет добавить оценку игры по 100-балльной шкале
        :param rating: Оценка игры

        Примеры:
        >>> game_test = VideoGame("Cuphead", "29.09.2017", "Studio MDHR")
        >>> game_test.add_review_grade(85)
        """
        if isinstance(rating, int):
            if 0 >= rating >= 100:
                self.review_grade = rating
            else:
                raise ValueError("Оценка игры должна быть от 0 до 100 баллов")
        else:
            raise TypeError(f"Не тот тип данных. Ожидается int, а не {type(rating)}")

    def __str__(self):
        """
        Магический метод __str__

        Примеры:
        >>> game_test = VideoGame("Cuphead", "29.09.2017", "Studio MDHR")
        >>> print(game_test)
        """
        return f"Игра {self.title}. Разработчик {self.developer}. Дата выхода: {self.release_date}"

    def __repr__(self):
        """
        Магический метод __repr__

        Примеры:
        >>> game_test = VideoGame("Cuphead", "29.09.2017", "Studio MDHR")
        >>> repr(game_test)
        """
        return f"{self.__class__.__name__}(title={self.title!r}, release date={self.release_date})"


class PCVersion(VideoGame):
    """ Версия игры для ПК """
    def __init__(self, title: str, release_date: str, developer: str, price_steam: float, min_required_windows_version: int):
        """
        Версия игры для PC
        :param title: Название игры
        :param release_date: Дата выхода
        :param developer: Разработчик игры
        :param price_steam: Цена в steam в американских долларах
        :param min_required_windows_version: Минимальные требования к версии Windows для установки

        Примеры:
        >>> PCVersion("Cuphead", "29.09.2017", "Studio MDHR", 19.99, 7)
        """
        super().__init__(title, release_date, developer) # Название, дата выхода и разработчик игры наследуются
        self.price_steam = price_steam
        self._min_required_windows_version = min_required_windows_version # Непубличный параметр, так как данные статичны
        self.review_grade = None # Параметр добавляется посредством метода add_review_grade, по умолчанию отсутствует

    @property
    def price_steam(self) -> float:
        """
        Геттер для параметра Цена в steam в американских долларах
        """
        return self.price_steam

    @price_steam.setter # На изменяемый параметр накладываются ограничения
    def price_steam(self, price_steam: float):
        """
        Сеттер для параметра Цена в steam в американских долларах
        :param price_steam: Новая цена игры в steam
        """
        if not isinstance(price_steam, float):
            return TypeError(f"Не тот тип данных. Ожидается float, а не {type(price_steam)}")
        if not price_steam > 0:
            return ValueError("Цена должна быть больше 0 долларов")
        self.price_steam = price_steam

    @property
    def min_required_windows_version(self):
        """
        Геттер для параметра Минимальные требования к версии Windows для установки
        """
        return self._min_required_windows_version

    def add_review_grade(self): # Перезагрузка метода так как в ПК версии используется иная система оценивания
        """
        Метод позволяет добавить оценку по критерию Рекомендую/Не рекомендую
        """
        ...

    def __str__(self): # Перезагрузка метода для добавлении информации о цене и требованиях к версии Windows
        """
        Магический метод __str__

        Примеры:
        >>> game_test = PCVersion("Cuphead", "29.09.2017", "Studio MDHR", 19.99, 7)
        >>> print(game_test)
        """
        return f"Игра {self.title}. Разработчик {self.developer}. Дата выхода: {self.release_date}. Цена: {self.price_steam} американских долларов. Требуется минимальная версия Windows: {self.min_required_windows_version}"

    def __repr__(self): # Перезагрузка метода для добавлении информации о цене и требованиях к версии Windows
        """
        Магический метод __repr__

        Примеры:
        >>> game_test = PCVersion("Cuphead", "29.09.2017", "Studio MDHR", 19.99, 7)
        >>> repr(game_test)
        """
        return f"{self.__class__.__name__}(title={self.title!r}, release date={self.release_date!r}, price_steam={self.price_steam!r}, min_required_windows_version={self.min_required_windows_version!r})"