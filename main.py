from timeit import timeit

from grayscale.clang.lib import dll
from grayscale.math import sum, mean, var, std


def create_data():
    return list(range(int(5e3)))


def perf():
    data = create_data()
    funs = [
        sum, mean, var, std,
    ]
    native_funs = [
        dll.sum, dll.mean, dll.var, dll.std,
    ]

    for fun, native_fun in zip(funs, native_funs):
        for times in [10, 100, 1000, 5000, 10000, 100000]:
            print('python ====')
            print(f'{times} times perf({fun.__name__}): {timeit(lambda: fun(data), number=times) * 1000}ms')

            print('clang ====')
            print(f'{times} times perf({native_fun.__name__}): {timeit(lambda: native_fun(data), number=times) * 1000}ms')


if __name__ == '__main__':
    perf()
