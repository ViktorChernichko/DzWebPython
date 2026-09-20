basketball_players = {}


def add_player():
    full_name = input("Введіть ПІБ гравця: ")
    height = input("Введіть зріст гравця (см): ")
    basketball_players[full_name] = height
    print("Гравця додано")


def remove_player():
    full_name = input("Введіть ПІБ гравця для видалення: ")
    if full_name in basketball_players:
        del basketball_players[full_name]
        print("Гравця видалено")
    else:
        print("Гравця не знайдено")


def find_player():
    full_name = input("Введіть ПІБ гравця для пошуку: ")
    if full_name in basketball_players:
        print(f"{full_name} - зріст {basketball_players[full_name]} см")
    else:
        print("Гравця не знайдено")


def update_player():
    full_name = input("Введіть ПІБ гравця для зміни: ")
    if full_name in basketball_players:
        new_height = input("Введіть новий зріст (см): ")
        basketball_players[full_name] = new_height
        print("Дані оновлено")
    else:
        print("Гравця не знайдено")


def show_all_players():
    if not basketball_players:
        print("Список порожній")
        return
    for full_name, height in basketball_players.items():
        print(f"{full_name} - {height} см")


def show_menu():
    print("\n1. Додати гравця")
    print("2. Видалити гравця")
    print("3. Знайти гравця")
    print("4. Змінити дані гравця")
    print("5. Показати всіх гравців")
    print("0. Вихід")


def main():
    while True:
        show_menu()
        choice = input("Виберіть дію: ")
        if choice == "1":
            add_player()
        elif choice == "2":
            remove_player()
        elif choice == "3":
            find_player()
        elif choice == "4":
            update_player()
        elif choice == "5":
            show_all_players()
        elif choice == "0":
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    main()
