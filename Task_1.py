#Vkontakte

class Vkontakte_user:
    def __init__(self, name: str, surname: str, age: int):
        """
        Создание и подготовка к работе объекта "Вконтакте пользователь"
        :param name: Имя пользователя
        :param surname: Фамилия пользователя
        Примеры:
        >>> user = Vkontakte_user('Ivan', 'Ivanov', 20)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError('Неправильный тип')
        if len(name) <= 0:
            raise ValueError('Имя должно быть длиннее 0 символов')
        self.name = name

        if not isinstance(surname, str):
            raise TypeError('Неправильный тип')
        if len(surname) <= 0:
            raise ValueError('Фамилия должна быть длиннее 0 символов')
        self.surname = surname

        if not isinstance(age, int):
            raise TypeError('Неправильный тип')
        if age <= 0:
            raise ValueError('Возраст должен быть больше 0')
        self.age = age

    def change_name(self, name: str, new_name: str):
        if not isinstance(new_name, str):
            raise TypeError('Неправильный тип')
        if len(new_name) <= 0:
            raise ValueError('Новое имя должно быть длиннее 0 символов')
        """
        Изменение имени пользователя
        :param name: имя пользователя
        :param new_name: новое имя пользователя
        :raise ValueError: Если новое имя пользователя совподает с текущим, то вызываем ошибку
        Примеры:
        >>> user = Vkontakte_user('Ivan', 'Ivanov', 20)
        >>> user.change_name('Ivan', 'Dimitry')
        """
        ...

    def change_surname(self, surname: str, new_surname: str):
        if not isinstance(new_surname, str):
            raise TypeError('Неправильный тип')
        if len(new_surname) <= 0:
            raise ValueError('Новая фамилия должна быть быть длиннее 0 символов')
        """
        Изменение фамилии пользователя
        :param surname: фамилия пользователя
        :param new_surname: новая фамилия пользователя
        :raise ValueError: Если новая фамилия пользователя совподает с текущей, то вызываем ошибку
        Примеры:
        >>> user = Vkontakte_user('Ivan', 'Ivanov', 20)
        >>> user.change_name('Ivanov', 'Smirnov')
        """
        ...

class Vkontakte_user_messages:
    def __init__(self, messages: int, unread_messages: int):
        if not isinstance(messages, int):
            raise TypeError('Неправильный тип')
        if not isinstance(unread_messages, int):
            raise TypeError('Неправильный тип')
        if unread_messages > messages:
            raise ValueError('Непрочитанных сообщений не может быть больше общего количества сообщений')
        """
        Создание и подготовка к работе объекта "Вконтакте сообщения пользователя"
        :param messages: Количество сообщений
        :param unread_messages: Количество непрочитанных сообщений
        Примеры:
        >>> user_friends = Vkontakte_user_messages(10, 2)  # инициализация экземпляра класса
        """
        if not isinstance(messages, int):
            raise TypeError('Неправильный тип')
        self.messages = messages

        if not isinstance(unread_messages, int):
            raise TypeError('Неправильный тип')
        self.unread_messages = unread_messages

    def new_message(self, unread_messages: int, new_message: int):
        if not isinstance(unread_messages, int):
            raise TypeError('Неправильный тип')
        if not isinstance(new_message, int):
            raise TypeError('Неправильный тип')
        """
        Появление нового непрочитанного сообщения
        :param unread_messages: Количество непрочитанных сообщений
        :param new_message: Количество новых непрочитанных сообщений
        Примеры:
        >>> user_friends = Vkontakte_user_friends(10, 2)
        >>> user_friends.new_message(2, 3)
        """
        ...

    def read_message(self, unread_messages: int, read_message: int):
        if not isinstance(unread_messages, int):
            raise TypeError('Неправильный тип')
        if not isinstance(credits(), int):
            raise TypeError('Неправильный тип')
        if read_message > unread_messages:
            raise ValueError('Прочитанных сообщений не может быть больше общего количества непрочитанных сообщений')
        """
        Прочтение непрочитанных сообщений
        :param unread_messages: Количество непрочитанных сообщений
        :param read_message: Количество прочитанных сообщений
        Примеры:
        >>> user_friends = Vkontakte_user_friends(10, 2)
        >>> user_friends.read_message(2, 1)
        """
        ...

class Vkontakte_user_friends:
    def __init__(self, friends: int, friends_requests: int):
        if not isinstance(friends, int):
            raise TypeError('Неправильный тип')
        self.friends = friends

        if not isinstance(friends_requests, int):
            raise TypeError('Неправильный тип')
        self.friends_requests = friends_requests

    def new_friends_requests(self, friends_requests: int, new_friends_requests: int):
        if not isinstance(friends_requests, int):
            raise TypeError('Неправильный тип')
        if not isinstance(new_friends_requests, int):
            raise TypeError('Неправильный тип')
        ...

    def delete_friends(self, friends: int, delete_friends: int):
        if not isinstance(friends, int):
            raise TypeError('Неправильный тип')
        if not isinstance(delete_friends, int):
            raise TypeError('Неправильный тип')
        if delete_friends > friends:
            raise ValueError('Количество удаленных друзей не может быть больше общего количества друзей')
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
