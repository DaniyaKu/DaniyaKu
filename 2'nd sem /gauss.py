import numpy as np

def gauss_for(A, B):
    n = len(B)
    for i in range(n):
        maxelem = abs(A[i][i])
        maxrow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxelem:
                maxelem = abs(A[k][i])
                maxrow = k
        for k in range(i, n):
            kt = A[maxrow][k]
            A[maxrow][k] = A[i][k]
            A[i][k] = kt
        kt = B[maxrow]
        B[maxrow] = B[i]
        B[i] = kt
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c*A[i][j]
            B[k] += c*B[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = B[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x

A = np.array([[2.7, 3.3, 1.3], [3.5, -1.7, 2.8], [4.1, 5.8, -1.7]]) # Матрица системы уравнений
B = np.array([2.1, 1.7, 0.8]) # Столбец свободных членов

x = gauss_for(A, B)

print("Результат:")
print(x)
