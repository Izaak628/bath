import numpy as np # ESC + L to show line number

primes_cache = []

def prime_decomposition_of(n):
    """Returns the prime decomposition of a number
    
    Input: Any natural number bigger than 2
    Output: Prime decomposition of that number e.g n = 24 would be {2: 3, 3: 1}
    """
    
    def add_new_prime(n):
        prime_factors[n] = 1
        if n not in primes_cache:
            primes_cache.append(n)
        
    if n != int(n):
        return Exception("Not a number")
    elif n < 2:
        return Exception("Not prime")
    
    prime_factors = {}
    d = 2
    while d**2 <= n:
        while n % d == 0:
            if d in prime_factors:
                prime_factors[d] += 1
            else:
                add_new_prime(d)
            n //= d
        d += 1
        
    if n > 1:
        add_new_prime(n)
    return prime_factors

def gcd(a, b):
    sum_of_numbers = 1
    for p in primes_cache:
        n = p ** min(a[p], b[p])
        sum_of_numbers *= n
    return sum_of_numbers

def lcm(a, b):
    sum_of_numbers = 1
    for p in primes_cache:
        n = p ** max(a[p], b[p])
        sum_of_numbers *= n
    return sum_of_numbers

# main code
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    a = prime_decomposition_of(num1)
    b = prime_decomposition_of(num2)

    # Gets all prime decomposition powers
    primes_cache.sort()
    for p in primes_cache:
        if p not in a:
            a[p] = 0
        elif p not in b:
            b[p] = 0

    print("\ngcd({}, {}) = {}".format(num1, num2, gcd(a, b)))
    print("lcm({}, {}) = {}".format(num1, num2, lcm(a, b)))
except:
    print(sys.exc_info())
