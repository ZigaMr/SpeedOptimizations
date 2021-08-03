from time import time
import numba

count = 1_00_00_000


def calulate_time(f):
    def wrapper(*args, **kwargs):
        start_time = time()
        output = f(*args, **kwargs)
        tot_time = time() - start_time
        print(f"{f.__name__} takes {tot_time} seconds")
        return output

    return wrapper


@calulate_time
@numba.jit(nopython=True)
def max_with_for_loop():
    max_value = 0
    for i in range(count):
        max_value = max(max_value, i)
    return max_value


@calulate_time
@numba.jit(nopython=True)
def max_with_while_loop():
    max_value = 0
    i = 0
    while i != count:
        max_value = max(max_value, i)
        i += 1
    return max_value


if __name__ == "__main__":
    max_with_for_loop()
    max_with_while_loop()
    max_with_for_loop()
    max_with_while_loop()