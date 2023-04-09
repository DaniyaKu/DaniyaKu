import random
import math

def integration(f, a, b, n):
    sum = 0.0
    sum_2 = 0.0

    for i in range(n):
        x = random.uniform(a, b)
        y = f(x)
        sum += y
        sum_2 += y**2

    mean = sum/n
    std_dev = math.sqrt(sum_2/n - mean**2)

    integral = (b-a)*mean

    error = (b-a)*std_dev/math.sqrt(n)

    return integral, error

integral, error = integration(math.sin, 0, 2*math.pi, 100000)

f = lambda x: 4*x**3
a = 0
b = 5
n = 10000
integral = integration(f, a, b, n)
print("Integral =", integral)