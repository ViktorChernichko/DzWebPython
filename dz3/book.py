class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Введіть назву книги: ")
        self.year = int(input("Введіть рік видання: "))
        self.publisher = input("Введіть видавця: ")
        self.genre = input("Введіть жанр: ")
        self.author = input("Введіть автора: ")
        self.price = float(input("Введіть ціну: "))

    def print_data(self):
        print(f"Назва: {self.title}")
        print(f"Рік видання: {self.year}")
        print(f"Видавець: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: {self.price} грн")

    def get_age(self, current_year):
        return current_year - self.year

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100
        return self.price

    def is_classic(self, years_threshold=50, current_year=2026):
        return self.get_age(current_year) >= years_threshold


if __name__ == "__main__":
    book = Book("Кобзар", 1840, "Дзюба", "Поезія", "Тарас Шевченко", 350)
    book.print_data()

    print(book.get_age(2026))
    print(book.apply_discount(15))
    print(book.is_classic())
