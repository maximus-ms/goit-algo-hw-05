def binary_search(data, value):
    """
    Performs binary search for float value in array.
    Returns tuple: number of iterations and a greater than or equal to the given value.
    """

    ix_l = 0
    ix_h = len(data) - 1
    iters = 0
    while ix_l < ix_h:
        ix_m = ix_l + (ix_h - ix_l) // 2
        iters += 1
        if data[ix_m] < value:
            ix_l = ix_m + 1
        elif data[ix_m] > value:
            ix_h = ix_m - 1
        else:
            ix_h = ix_m
    return iters, data[ix_h]


def main():
    from numpy import random

    num = random.randint(2048)
    data = random.random(size=(num))
    data.sort()
    value = random.random()
    iters, res = binary_search(data, value)
    print(f"Size of array: {num}")
    print(f"Value to search: {value}")
    print(f"Received value from array: {res}")
    print(f"Iterations to search: {iters}")


if __name__ == "__main__":
    main()
