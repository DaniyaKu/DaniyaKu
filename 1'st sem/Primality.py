def primality(n):
    if n % 2 == 0:
        return n == 2
    else:
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n

print(primality(29)) # True
print(primality(169)) # False
