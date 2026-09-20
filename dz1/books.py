books = {}


def add_book():
    title = input("Введіть назву книги: ")
    author = input("Введіть автора: ")
    genre = input("Введіть жанр: ")
    year = input("Введіть рік випуску: ")
    pages = input("Введіть кількість сторінок: ")
    publisher = input("Введіть видавництво: ")
    books[title] = {
        "author": author,
        "genre": genre,
        "year": year,
        "pages": pages,
        "publisher": publisher,
    }
    print("Книгу додано")


def remove_book():
    title = input("Введіть назву книги для видалення: ")
    if title in books:
        del books[title]
        print("Книгу видалено")
    else:
        print("Книгу не знайдено")


def print_book_card(title):
    data = books[title]
    print(f"Назва: {title}")
    print(f"Автор: {data['author']}")
    print(f"Жанр: {data['genre']}")
    print(f"Рік випуску: {data['year']}")
    print(f"Сторінок: {data['pages']}")
    print(f"Видавництво: {data['publisher']}")


def find_book():
    title = input("Введіть назву книги для пошуку: ")
    if title in books:
        print_book_card(title)
    else:
        print("Книгу не знайдено")


def update_book():
    title = input("Введіть назву книги для зміни: ")
    if title not in books:
        print("Книгу не знайдено")
        return
    print("Що змінити?")
    print("1. Автор")
    print("2. Жанр")
    print("3. Рік випуску")
    print("4. Кількість сторінок")
    print("5. Видавництво")
    field_choice = input("Виберіть пункт: ")
    field_map = {
        "1": "author",
        "2": "genre",
        "3": "year",
        "4": "pages",
        "5": "publisher",
    }
    if field_choice in field_map:
        new_value = input("Введіть нове значення: ")
        books[title][field_map[field_choice]] = new_value
        print("Дані оновлено")
    else:
        print("Невірний вибір")


def show_all_books():
    if not books:
        print("Колекція порожня")
        return
    for title in books:
        print_book_card(title)
        print("-" * 20)


def show_menu():
    print("\n1. Додати книгу")
    print("2. Видалити книгу")
    print("3. Знайти книгу")
    print("4. Змінити дані книги")
    print("5. Показати всі книги")
    print("0. Вихід")


def main():
    while True:
        show_menu()
        choice = input("Виберіть дію: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            find_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            show_all_books()
        elif choice == "0":
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    main()
