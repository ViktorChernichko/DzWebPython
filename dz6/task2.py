import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
    return wrapper


@execution_time
def find_prime_numbers(range_start=0, range_end=1000):
    primes = []
    for number in range(max(2, range_start), range_end + 1):
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


if __name__ == "__main__":
    result_1 = find_prime_numbers()
    print(f"Prime numbers from 0 to 1000: {len(result_1)}")
    print(result_1)

    result_2 = find_prime_numbers(100, 200)
    print(f"Prime numbers from 100 to 200: {len(result_2)}")
    print(result_2)
