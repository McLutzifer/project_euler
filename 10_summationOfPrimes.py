#Sieve of Atkins
import pprint

limit = 2000000
s = [1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59]
s_1 = [1, 13, 17, 29, 37, 41, 49, 53]
s_2 = [7, 19, 31, 43]
s_3 = [11, 23, 47, 59]
d = 60



new_list = []


def primeNumber(n):
    prime = [True for i in range(limit + 1)]
    p = 2

    while p*p <= n:
        if (prime[p] == True):
            for i in range (p*2, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            new_list.append(p)


primeNumber(limit)
print(sum(new_list))

# 142913828922