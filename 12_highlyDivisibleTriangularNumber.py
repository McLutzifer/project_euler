import numpy as np

triangleNumbers = []
x = 0
for i in range (1,90000):
	x = x+i
	triangleNumbers.append(x)
print(triangleNumbers)

'''
for j in range(8, 11):
	for k in range (1, triangleNumbers[j]):
		print(triangleNumbers[j]%k)
'''

for num in triangleNumbers:
	count = 0
	for i in range (2, 11000):
		if num%i == 0:
			count += 1
	if count  >= 499:
		print(str(count) + " the number is " + str(num))



			#236215980 wrong