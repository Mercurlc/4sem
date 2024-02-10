import math


def main(x, z, y):
    chislitel = math.exp(5 * (88 * z ** 3 + y ** 2 / 66 + 92 * x))
    num_znamenatel = 48
    znamenatel = 60 * (y - 27 * x ** 3) ** 5 - z ** 4
    first_frac = chislitel/num_znamenatel/znamenatel

    second_chislitel = 19 * z ** 4 - (x ** 3 - y)
    second_znamenatel = 70 * (18 - 59 * x ** 3 - y ** 2) ** 2 - 94 * z ** 3
    second_frac = second_chislitel/second_znamenatel

    return first_frac - second_frac


print(main(-0.1, -0.77, 0.94))