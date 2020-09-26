'''
n = 0
for n in range(0, 2527):
    i = 1
    while i <= 20:
        if n%i == 0:
            i = i+1
            print('i ist ', i)
            print('n ist ', n)
        else:
            n = n+1
    print(n)


n = 0
for n in range (1,2700):
    i = 1
    if (n%i for i in range (1,11)) == 0:
        print('n is: ', n, 'i is: ', i )
        i = i+1
        n = n+1

        232792560

'''

n = 0
for n in range (1, 260000000):
    if all (n%i == 0 for i in range (1,21):
        return n
    return None