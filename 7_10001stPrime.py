def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = 3

counter = 2

while counter <= 10001:
    if isprime(x):
        counter += 1
        x += 2
    else:
        x += 2

print(x-2)  # 104743


"""def nth_prime(n):
    counter = 2
    for i in range(3, n**2, 2):
        k = 1
        while k*k < i:
            k += 2
            if i % k == 0:
               break
        else:
            counter += 1
        if counter == n:
            return i

print(nth_prime(100001))

#1299721 ist antwort
"""

'''prime = []

while len(prime) <= 10002:
    for num in range (2, 105000):
        for i in range(num, 2, -1):
            if num % i == 0:
                break
    else:
        prime.append(num)

print(prime)
'''