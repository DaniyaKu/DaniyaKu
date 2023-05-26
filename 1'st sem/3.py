import GCD_module

"""
По трем заданным коэффициентам диофантового уравнения определяет, есть решение или нет
"""
a = int(input())
b = int(input())
c = int(input())

gcd = GCD_module.Euclid_algorithm(abs(a), abs(b)) 
if abs(c)//gcd:
    print("Решение есть")
else:
    print("Решений нет") 
