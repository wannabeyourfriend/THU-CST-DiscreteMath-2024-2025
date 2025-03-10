def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)
def f(n):
    if n == 0:
        return 1
    else:
        return 1.0 + 1.0 / f(n - 1)
for n in range(10):
        print(f(n))
print('*'*20)
def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2:
        return fib2((n+1) / 2 - 1) * fib2((n+1) / 2 - 1) + fib2((n+1) / 2) * fib2((n+1) / 2)
    else:
        return (2 * fib2(n/2 - 1)+ fib2(n / 2)) * fib2((n / 2))
if __name__=="__main__":
    for (a,n) in [(0, 0), (10, 0), (20, 2), (12, 4), (30, 10)]:
        print(power(a, n))

    print('*'*20)

    for n in range(10):
        print(fib(n))


    print('*' * 20)

    for (m,n) in [(12,3), (12, 31), (24,13), (2,1237000)]:
        print(gcd(m,n))

    print('*' * 20)

    for n in range(10):
        print(f(n))

    print('*' * 20)

    for n in range(11):
        print(fib2(n))
