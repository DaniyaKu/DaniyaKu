def Extended_Euclidean(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = Extended_Euclidean(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)

d = Extended_Euclidean(792, 684)
print(f"НОД равен {d[0]}, x = {d[1]}, y = {d[2]}")

# НОД равен 36, x = -6, y = 7
