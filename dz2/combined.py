def digit_length_stats(numbers):
    stats = {}
    for number in numbers:
        length = len(str(abs(number)))
        stats[length] = stats.get(length, 0) + 1
    return stats


def cheapest_product(products):
    cheapest = min(products, key=lambda product: product["price"])
    return cheapest["name"]


def group_by_first_letter(words):
    groups = {}
    for word in words:
        letter = word[0]
        groups.setdefault(letter, []).append(word)
    return groups


def split_even_odd(numbers):
    even = {number for number in numbers if number % 2 == 0}
    odd = {number for number in numbers if number % 2 != 0}
    return even, odd


def analyze_text(text):
    words = text.lower().split()
    unique_words = set(words)
    most_common = max(set(words), key=words.count)
    return len(unique_words), most_common


def save_to_db(**kwargs):
    for field, value in kwargs.items():
        print(f"Запис у БД: {field} = {value}")


if __name__ == "__main__":
    print(digit_length_stats([1, 22, 333, 4, 55, 666, 7]))

    products = [
        {"name": "Хліб", "price": 25},
        {"name": "Молоко", "price": 40},
        {"name": "Яйця", "price": 60},
    ]
    print(cheapest_product(products))

    words = ["кіт", "коза", "птах", "пес", "піч"]
    print(group_by_first_letter(words))

    even, odd = split_even_odd([1, 2, 3, 4, 5, 6])
    print(even, odd)

    sentence = input("Введіть речення: ")
    unique_count, most_common_word = analyze_text(sentence)
    print(unique_count, most_common_word)

    save_to_db(name="Іван", age=25, city="Київ")
