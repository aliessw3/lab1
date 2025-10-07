def divisors(n):
    t = 0
    for i in range(1, n + 1):
        if n % i == 0:
            t += 1
    return t
n=int(input("Enter n: "))
print(divisors(n))
