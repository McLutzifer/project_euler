def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r

for n in range (998001, 10000, -1):
    if n == reverse_number(n):
        print(reverse_number(n))



print('#########################')

import sys
for i in range(100,1000):
   for j in range(100,1000):
      k = i*j
      if k == reverse_number(k):
        if k > 888888:
            print (k)
   print()




   906609
