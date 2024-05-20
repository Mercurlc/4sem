
from math import ceil

def f_corrected(x, z, y):
    n = len(y)
    sum_expression = 0
    for i in range(1, n+1):
        sum_expression += 20 * (4 * y[i-1] + x[n - ceil(i/4)]**2 + 46 * z[ceil(i/2)-1]**3)
    return 19 * (sum_expression**7)