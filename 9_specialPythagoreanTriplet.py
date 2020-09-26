x = 1000

#ab_list = list(range(1, 101))
#c_list = list(range(1, 101))

for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            y=a+b+c
            if a<b and b<c:
                if y == x:
                    if (a**2 + b**2 == c**2):
                        print(y, 'abc is ', a,b,c)
