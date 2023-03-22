import math;
import random as random_number;
def MCint3(f, a, b, n, N=100):
    s = 0;  I_values = []; k_values = [];
    for k in range(1, n+1):
        x = random_number.uniform(a, b);
        s += f(x);
        if( k  %  N )  ==  0:
            I = (float(b-a)/k)*s;
            print(I);
            I_values.append(I);
            k_values.append(k);
    return k_values, I_values;
 # Подъинтегральная функция  
def f1(x):
    return (math.exp(-x*x));
# Вызов функции 
k, I = MCint3(f1, 1, 2, 1000000, N=1000000);