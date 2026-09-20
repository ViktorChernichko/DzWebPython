employees = {}


def add_employee():
    full_name = input("Введіть ПІБ працівника: ")
    phone = input("Введіть телефон: ")
    email = input("Введіть корпоративний email: ")
    position = input("Введіть назву посади: ")
    room = input("Введіть номер кабінету: ")
    skype = input("Введіть Skype: ")
    employees[full_name] = {
        "phone": phone,
        "email": email,
        "position": position,
        "room": room,
        "skype": skype,
    }
    print("Працівника додано")


def remove_employee():
    full_name = input("Введіть ПІБ працівника для видалення: ")
    if full_name in employees:
        del employees[full_name]
        print("Працівника видалено")
    else:
        print("Працівника не знайдено")


def print_employee_card(full_name):
    data = employees[full_name]
    print(f"ПІБ: {full_name}")
    print(f"Телефон: {data['phone']}")
    print(f"Email: {data['email']}")
    print(f"Посада: {data['position']}")
    print(f"Кабінет: {data['room']}")
    print(f"Skype: {data['skype']}")


def find_employee():
    full_name = input("Введіть ПІБ працівника для пошуку: ")
    if full_name in employees:
        print_employee_card(full_name)
    else:
        print("Працівника не знайдено")


def update_employee():
    full_name = input("Введіть ПІБ працівника для зміни: ")
    if full_name not in employees:
        print("Працівника не знайдено")
        return
    print("Що змінити?")
    print("1. Телефон")
    print("2. Email")
    print("3. Посада")
    print("4. Кабінет")
    print("5. Skype")
    field_choice = input("Виберіть пункт: ")
    field_map = {
        "1": "phone",
        "2": "email",
        "3": "position",
        "4": "room",
        "5": "skype",
    }
    if field_choice in field_map:
        new_value = input("Введіть нове значення: ")
        employees[full_name][field_map[field_choice]] = new_value
        print("Дані оновлено")
    else:
        print("Невірний вибір")


def show_all_employees():
    if not employees:
        print("Список порожній")
        return
    for full_name in employees:
        print_employee_card(full_name)
        print("-" * 20)


def show_menu():
    print("\n1. Додати працівника")
    print("2. Видалити працівника")
    print("3. Знайти працівника")
    print("4. Змінити дані працівника")
    print("5. Показати всіх працівників")
    print("0. Вихід")


def main():
    while True:
        show_menu()
        choice = input("Виберіть дію: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            find_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            show_all_employees()
        elif choice == "0":
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    main()
