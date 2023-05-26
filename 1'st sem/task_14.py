from typeguard import typechecked

"""
    Реализация с помощью декоратора на основе тестиков
"""
@typechecked
def Euclid_algorithm(num1: int, num2: int) -> int:
    assert a >= 0  # Дополнительная проверка на неотрицательность
    assert b >= 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1 or num2

try:
    a = 10
    b = 20
    print(Euclid_algorithm(a, b))
    print('Тест 1 -- успешно')
except:
    print('Тест 1 -- провал')

try:
    a = '10'
    b = 20
    print(Euclid_algorithm(a, b))
    print('Тест 2 -- успешно')
except:
    print('Тест 2 -- провал')

try:
    a = 10.23
    b = 20
    print(Euclid_algorithm(a, b))
    print('Тест 4 -- успешно')
except:
    print('Тест 3 -- провал')

try:
    a = 10
    b = 20.0
    print(Euclid_algorithm(a, b))
    print('Тест 4 -- успешно')
except:
    print('Тест 4 -- провал')

try:
    a = -10
    b = 20
    print(Euclid_algorithm(a, b))
    print('Тест 5 -- успешно')
except:
    print('Тест 5 -- провал')
    
