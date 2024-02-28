def main(n):
    if n == 0:
        return -0.43
    if n == 1:
        return -0.12
    if n >= 2:
        return main(n - 2) ** 2 + 32 * main(n - 1) ** 3


print(main(6))
