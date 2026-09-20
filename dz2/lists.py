def sort_by_length(names):
    return sorted(names, key=len)


def every_second(data):
    return data[::2]


def reverse_list(data):
    return data[::-1]


def filter_even(numbers):
    return [number for number in numbers if number % 2 == 0]


def zip_to_dict(keys, values):
    return dict(zip(keys, values))


def matrix_center(matrix):
    return matrix[1][1]


if __name__ == "__main__":
    names = ["Anna", "Oleksandr", "Ivan", "Danylo"]
    print(sort_by_length(names))

    print(every_second(names))

    print(reverse_list(names))

    print(filter_even([1, 2, 3, 4, 5, 6]))

    keys = ["id", "name"]
    values = [1, "Admin"]
    print(zip_to_dict(keys, values))

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix_center(matrix))
