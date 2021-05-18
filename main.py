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
            print(f'{times} times perf: {timeit(lambda: fun(data), number=times)}s')

            print('clang ====')
            print(f'{times} times perf: {timeit(lambda: native_fun(data), number=times)}s')


if __name__ == '__main__':
    perf()
