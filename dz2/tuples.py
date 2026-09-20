def get_user():
    return "Іван", 25, "Київ"


def unpack_points(points):
    for x, y in points:
        print(f"X: {x}, Y: {y}")


def split_tuple(numbers):
    first, second, *rest = numbers
    return first, second, rest


def swap(a, b):
    a, b = b, a
    return a, b


def sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average


def try_change_city_tuple():
    cities = ("Київ", "Львів", "Одеса", "Харків", "Дніпро")
    try:
        cities[0] = "Полтава"
    except TypeError as error:
        print(f"Помилка: {error}")


if __name__ == "__main__":
    name, age, city = get_user()
    print(name, age, city)

    points = [(1, 2), (3, 4), (5, 6)]
    unpack_points(points)

    numbers = tuple(range(1, 11))
    first, second, rest = split_tuple(numbers)
    print(first, second, rest)

    a, b = 5, 10
    a, b = swap(a, b)
    print(a, b)

    total, average = sum_and_average([1, 2, 3, 4, 5])
    print(total, average)

    try_change_city_tuple()
