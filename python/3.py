from math import sin


def func(i, j, c):
    return i - sin(j) ** 5 - 4 * (61 * c ** 2 - 2 * j) ** 7


def main(n, m, a):
    sum = 0
    for c in range(1, a + 1):
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum += func(i, j, c)
    return sum


print(main(3, 5, 3))
