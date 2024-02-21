from math import log


def main(z):
    if z < -53:
        return 93 * z
    if -53 <= z < 23:
        return z
    if z >= 23:
        return (88 * z ** 2 + z / 66) ** 3 - z ** 2 / 7 - 79 * log(z) ** 4


print(main(52))
