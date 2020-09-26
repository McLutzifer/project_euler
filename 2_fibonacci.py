def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range (2,n):
            c = a+b
            a = b
            b = c
            if c > 4000000:
                break
        return b


even = [fibonacci(x) for x in range (80) if fibonacci(x)%2 == 0]


print(even)

print(sum(even))
