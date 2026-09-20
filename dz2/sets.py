import random


def compare_clubs(math_club, science_club):
    math_set = set(math_club)
    science_set = set(science_club)
    both = math_set & science_set
    only_math = math_set - science_set
    all_students = math_set | science_set
    return both, only_math, all_students


def is_unique(data):
    return len(data) == len(set(data))


def remove_duplicates(data):
    return list(set(data))


def has_ten(numbers_set):
    return 10 in numbers_set


def is_subset(first_set, second_set):
    return first_set.issubset(second_set)


def safe_discard(data_set, element):
    data_set.discard(element)
    return data_set


if __name__ == "__main__":
    math_club = ["Ivan", "Olga", "Petro"]
    science_club = ["Olga", "Maria", "Ivan"]
    both, only_math, all_students = compare_clubs(math_club, science_club)
    print(both, only_math, all_students)

    print(is_unique([1, 2, 3]))
    print(is_unique([1, 2, 2]))

    print(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5]))

    random_numbers = {random.randint(1, 20) for _ in range(10)}
    print(random_numbers, has_ten(random_numbers))

    print(is_subset({1, 2}, {1, 2, 3}))

    numbers_set = {1, 2, 3}
    print(safe_discard(numbers_set, 5))
