import numpy as np


def is_prime(n: int) -> bool:
    n = abs(n)
    if n in [0, 1]:
        return False

    if n in [2, 3]:
        return True

    # if even, not prime
    if ((n % 10) % 2) == 0:
        return False

    # if greater than 5 and ends in 5, not prime
    if (n > 5) and (n % 10) == 5:
        return False

    # if > 3 and sum of digits divisible by 3, not prime
    sum_digits = 0
    for digit in str(n):
        sum_digits += int(digit)
    if (sum_digits % 3) == 0:
        return False

    for potential_factor in range(3, int(np.sqrt(n)+1), 2):
        if (n % potential_factor) == 0:
            return False

    return True


if __name__ == '__main__':
    primes = []
    for i in range(200):
        if is_prime(i):
            primes.append(i)

    print(primes)
    print(len(primes))
