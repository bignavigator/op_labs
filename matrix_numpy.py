import numpy as np


def func_f(x):
    return np.power(np.e, -2*x)-x


def func_g(x):
    return np.sqrt(x)+1/np.power(np.e, x)


def func_a_ij(i, j):
    return np.fabs(func_f(i) + func_g(j))


def func_n_a(m, n):
    min_value = float("inf")
    max_value = float("-inf")

    for i in range(1, m+1):
        for j in range(1, n+1):
            min_value = min(min_value, func_a_ij(i, j))
            max_value = max(max_value, func_a_ij(i, j))

    return ((min_value+1)/(max_value+1))-1


if __name__ == "__main__":
    print(func_n_a(10, 10))
