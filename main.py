from timeit import timeit

from grayscale.clang.math import sum as c_sum
from grayscale.clang.math import mean as c_mean
from grayscale.clang.math import var as c_var
from grayscale.clang.math import std as c_std
from grayscale.clang.math import min as c_min
from grayscale.clang.math import max as c_max
from grayscale.math import sum
from grayscale.math import mean
from grayscale.math import var
from grayscale.math import std
from grayscale.math import min
from grayscale.math import max


def create_data():
    return list(range(int(5e3)))


def perf():
    data = create_data()
    funs = [
        sum, mean, var, std, min, max,
    ]
    native_funs = [
        c_sum, c_mean, c_var, c_std, c_min, c_max,
    ]

    for fun, native_fun in zip(funs, native_funs):
        for times in [10, 100, 1000, 5000, 10000, 100000]:
            print('python ====')
            print(f'{times} times perf({fun.__name__}): {timeit(lambda: fun(data), number=times) * 1000}ms')

            print('clang ====')
            print(f'{times} times perf({native_fun.__name__}): {timeit(lambda: native_fun(data), number=times) * 1000}ms')


if __name__ == '__main__':
    perf()
