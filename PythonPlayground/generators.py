import time


def multiple(number, maximum):
    counter = 1
    multiple_list = []
    value = number * counter

    while value <= maximum:
        multiple_list.append(value)
        value = number * counter
        counter += 1

    return multiple_list


def multiple_gen(number, maximum):
    counter = 1
    value = number * counter

    while value <= maximum:
        yield value
        counter += 1
        value = number * counter


if __name__ == '__main__':
    MULTIPLE = 463
    MAX = 100_000_000_000

    start_time = time.time()
    for number in multiple_gen(MULTIPLE, MAX):
        pass
    print(f"Generator took {time.time() - start_time: .2f}")

    start_time = time.time()
    for number in multiple(MULTIPLE, MAX):
        pass
    print(f"Normal list took {time.time() - start_time: .2f}")
