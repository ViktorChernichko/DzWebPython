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
def find_prime_numbers():
    primes = []
    for number in range(2, 1001):
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes


if __name__ == "__main__":
    result = find_prime_numbers()
    print(f"Prime numbers found: {len(result)}")
    print(result)
