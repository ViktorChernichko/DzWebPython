english_french_dict = {}


def add_word():
    english_word = input("Введіть слово англійською: ")
    french_word = input("Введіть переклад французькою: ")
    english_french_dict[english_word] = french_word
    print("Слово додано")


def remove_word():
    english_word = input("Введіть слово англійською для видалення: ")
    if english_word in english_french_dict:
        del english_french_dict[english_word]
        print("Слово видалено")
    else:
        print("Слово не знайдено")


def find_word():
    english_word = input("Введіть слово англійською для пошуку: ")
    if english_word in english_french_dict:
        print(f"{english_word} - {english_french_dict[english_word]}")
    else:
        print("Слово не знайдено")


def update_word():
    english_word = input("Введіть слово англійською для зміни: ")
    if english_word in english_french_dict:
        new_translation = input("Введіть новий переклад французькою: ")
        english_french_dict[english_word] = new_translation
        print("Дані оновлено")
    else:
        print("Слово не знайдено")


def show_all_words():
    if not english_french_dict:
        print("Словник порожній")
        return
    for english_word, french_word in english_french_dict.items():
        print(f"{english_word} - {french_word}")


def show_menu():
    print("\n1. Додати слово")
    print("2. Видалити слово")
    print("3. Знайти слово")
    print("4. Змінити переклад")
    print("5. Показати весь словник")
    print("0. Вихід")


def main():
    while True:
        show_menu()
        choice = input("Виберіть дію: ")
        if choice == "1":
            add_word()
        elif choice == "2":
            remove_word()
        elif choice == "3":
            find_word()
        elif choice == "4":
            update_word()
        elif choice == "5":
            show_all_words()
        elif choice == "0":
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    main()
