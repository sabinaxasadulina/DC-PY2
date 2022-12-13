import doctest
#Vkontakte

class VkontakteUser:
    def __init__(self, name: str, surname: str, age: int):
        """
        Создание и подготовка к работе объекта "Вконтакте пользователь"
        :param name: Имя пользователя
        :param surname: Фамилия пользователя
        :raise ValueError: Если возвраст пользователя меньше 0, то вызываем ошибку
        Примеры:
        >>> user = VkontakteUser('Ivan', 'Ivanov', 20)
        """
        if not isinstance(name, str):
            raise TypeError('Неправильный тип')
        self.name = name

        if not isinstance(surname, str):
            raise TypeError('Неправильный тип')
        self.surname = surname

        if not isinstance(age, int):
            raise TypeError('Неправильный тип')
        if age <= 0:
            raise ValueError('Возраст должен быть больше 0')
        self.age = age

    def change_name(self, name: str, new_name: str):
        """
        Изменение имени пользователя
        :param name: имя пользователя
        :param new_name: новое имя пользователя
        :raise ValueError: Если новое имя пользователя совпадает с текущим, то вызываем ошибку
        Примеры:
        >>> user = VkontakteUser('Ivan', 'Ivanov', 20)
        >>> user.change_name('Ivan', 'Dimitry')
        """
        if not isinstance(new_name, str):
            raise TypeError('Неправильный тип')
        if new_name == name:
            raise ValueError('Новое имя пользователя не должно совпадать с текущим')
        ...

    def change_surname(self, surname: str, new_surname: str):
        """
        Изменение фамилии пользователя
        :param surname: фамилия пользователя
        :param new_surname: новая фамилия пользователя
        :raise ValueError: Если новая фамилия пользователя совподает с текущей, то вызываем ошибку
        Примеры:
        >>> user = VkontakteUser('Ivan', 'Ivanov', 20)
        >>> user.change_surname('Ivanov', 'Smirnov')
        """
        if not isinstance(new_surname, str):
            raise TypeError('Неправильный тип')
        if new_surname == surname:
            raise ValueError('Новая фамилия пользователя не должна совпадать с текущим')
        ...

class VkontakteUserMessages:
    def __init__(self, messages: int, unread_messages: int):
        """
        Создание и подготовка к работе объекта "Вконтакте сообщения пользователя"
        :param messages: Количество сообщений
        :param unread_messages: Количество непрочитанных сообщений
        :raise ValueError: Если количество непрочитанных сообщений превышает общее количествво сообщений пользователя, то вызываем ошибку
        Примеры:
        >>> user_messages = VkontakteUserMessages(10, 2)
        """
        if not isinstance(messages, int):
            raise TypeError('Неправильный тип')
        self.messages = messages

        if not isinstance(unread_messages, int):
            raise TypeError('Неправильный тип')
        if unread_messages > messages:
            raise ValueError('Непрочитанных сообщений не может быть больше общего количества сообщений')
        self.unread_messages = unread_messages

    def add_new_message(self, messages: int, new_messages: int):
        """
        Появление нового сообщения
        :param messages: Количество сообщений
        :param new_messages: Количество новых сообщений
        Примеры:
        >>> user_messages = VkontakteUserMessages(10, 2)
        >>> user_messages.add_new_message(10, 1)
        """
        if not isinstance(messages, int):
            raise TypeError('Неправильный тип')
        if not isinstance(new_messages, int):
            raise TypeError('Неправильный тип')
        ...

    def read_message(self, messages: int, read_messages: int):
        """
        Прочтение сообщений
        :param messages: Количество сообщений
        :param read_messages: Количество прочитанных пользователем сообщений
        :raise ValueError: Если количество прочитанных сообщений превышает общее количествво сообщений пользователя, то вызываем ошибку
        Примеры:
        >>> user_messages = VkontakteUserMessages(10, 2)
        >>> user_messages.read_message(10, 1)
        """
        if not isinstance(messages, int):
            raise TypeError('Неправильный тип')
        if not isinstance(read_messages, int):
            raise TypeError('Неправильный тип')
        if read_messages > messages:
            raise ValueError('Прочитанных сообщений не может быть больше общего количества сообщений')
        ...

class VkontakteUserFriends:
    def __init__(self, friends: int, friends_requests: int):
        """
        Создание и подготовка к работе объекта "Вконтакте друзья пользователя"
        :param friends: Количество друзей
        :param friends_requests: Количество заявок в друзья
        Примеры:
        >>> user_friends = VkontakteUserFriends(20, 3)
        """
        if not isinstance(friends, int):
            raise TypeError('Неправильный тип')
        self.friends = friends

        if not isinstance(friends_requests, int):
            raise TypeError('Неправильный тип')
        self.friends_requests = friends_requests

    def add_new_friends_requests(self, friends_requests: int, new_friends_requests: int):
        """
        Увеличение заявок в друзья
        :param friends_requests: Количество заявок в друзья
        :param new_friends_requests: Количество новых заявок в друзья
        Примеры:
        >>> user_friends = VkontakteUserFriends(20, 3)
        >>> user_friends.add_new_friends_requests(3, 2)
        """
        if not isinstance(friends_requests, int):
            raise TypeError('Неправильный тип')
        if not isinstance(new_friends_requests, int):
            raise TypeError('Неправильный тип')
        ...

    def delete_friends_from_friends(self, friends: int, delete_friends: int):
        """
        Удаление друзей из списка друзей пользователя
        :param friends: Количество друзей
        :param delete_friends: Количество удаленных друзей
        :raise ValueError: Если количество друзей на удаление превышает общее количество друзей пользователя, то вызываем ошибку
        Примеры:
        >>> user_friends = VkontakteUserFriends(20, 3)
        >>> user_friends.delete_friends_from_friends(20, 5)
        """
        if not isinstance(friends, int):
            raise TypeError('Неправильный тип')
        if not isinstance(delete_friends, int):
            raise TypeError('Неправильный тип')
        if delete_friends > friends:
            raise ValueError('Количество друзей на удаление не может быть больше общего количества друзей')
        ...

if __name__ == "__main__":
    doctest.testmod()
