def increase_bananas(inventory, amount):
    inventory["banana"] += amount
    return inventory


def count_chars(text):
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result


def print_keys_above(data, threshold):
    for key, value in data.items():
        if value > threshold:
            print(key)


def squares_dict():
    return {number: number ** 2 for number in range(1, 6)}


def merge_dicts(d1, d2):
    return {**d1, **d2}


def safe_get(data, key):
    return data.get(key, "Не знайдено")


if __name__ == "__main__":
    inventory = {"apple": 5, "banana": 10, "orange": 8}
    print(increase_bananas(inventory, 3))

    print(count_chars("привіт"))

    print_keys_above(inventory, 5)

    print(squares_dict())

    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    print(merge_dicts(d1, d2))

    print(safe_get(inventory, "apple"))
    print(safe_get(inventory, "melon"))
