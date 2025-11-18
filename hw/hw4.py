
class Book:

    def __init__(self, title, author, pages, format="бумажная" ):
        self.title = title
        self.author = author
        self.pages = pages
        self.format = format

    def __str__(self):
        return f'"{self.title}" — {self.author}, {self.pages} стр.'

    def __len__(self):
        return self.pages

    def __add__(self, other):
        total = self.pages + other.pages
        return total

    def __eq__(self, other):
        return self.pages == other.pages

    def __getitem__(self, item):
        return f"Глава {item}: содержание книги '{self.title}'"

    @classmethod
    def from_string(cls, s):
        title, author, pages = s.split(", ")
        return cls(title, author, int(pages))


    @staticmethod
    def is_thick(pages):
        return pages > 500

# Обычное создание
book1 = Book("1984", "Дж. Оруэлл", 328)

# Через класс-метод
book2 = Book.from_string("Гарри Поттер, Дж. Роулинг, 400")

# Магические методы
print(book1)                    # "1984" — Дж. Оруэлл, 328 стр.
print(len(book1))               # 328
print(book1 + book2)            # Вместе: 728 страниц
print(book1 == book2)           # False
print(book1[5])                 # Глава 5: содержание книги '1984'

# Статический метод
print(Book.is_thick(600))       # True
print(Book.is_thick(300))       # False

# Формат по умолчанию
book3 = Book("Python", "Гвидо", 200)
print(book3.format)             # бумажная
