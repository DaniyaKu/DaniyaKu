def Euclid_algorithm(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1 or num2


a = Euclid_algorithm(756, 238)
print(a)  # будет 14
