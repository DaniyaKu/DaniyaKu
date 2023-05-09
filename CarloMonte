import numpy as np

def montecarlo(func,
            a = 0,
            b = 1,
            n = 1000):
    
    subsets = np.arange(0, n+1, n/10)
    steps = n/10
    u = np.zeros(n)
    for i in range(10):
        start = int(subsets[i])
        end = int(subsets[i+1])
        u[start:end]=np.random.uniform(low=i/10,high=(i+1)/10,size=end-start)
    np.random.shuffle(u)

    u_func = func(a+(b-a)*u)
    s = ((b-a)/n)-u_func.sum()

    return s

def func(x):
    return (17*x**4+21*x**2+x)**(-1/2)

integral = montecarlo(func, a=0,b=4,n=1000)
print(integral)
