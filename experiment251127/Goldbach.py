def isPrime(n): #判断n是否为素数
    if n < 2:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

def TwoPrimes(n):
    for p in range(2, n):
        q = n - p
        if isPrime(p) and isPrime(q):
            return p, q

for n in range(4, 101, 2):
    p, q = TwoPrimes(n)
    print(n, "=", p, "+", q)
