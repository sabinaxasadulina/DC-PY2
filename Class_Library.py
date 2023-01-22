from pydantic import BaseModel


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
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: Индекс книги
        :param name: Название книги
        :param pages: Количество страниц
        Примеры:
        >>> book = Book(1, "Война и мир", 1300)
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

class Library:
    def __init__(self, books = None):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: Список книг
        >>> library = Library(0)
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """
        Добавление новой книги в библиотеку с назначением возрастающего идентификатора
        :return: Назначенный идентификатор новой книги, если книга первая, то присваивается идентификатор 1
        """
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int):
        """
        Поиск книги в библиотеке по идентификатору
        :raise ValueError: Если запрашиваемого идентификатора книги не существует в списке библиотеки
        :return: индекс запрашиваемой книги в библиотеке
        """
        for index, book in enumerate(self.books):
            if book.id_ == id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует!")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
