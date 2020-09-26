import operator

# n/2 if even
# 3n + 1 if odd



new_list = []

in_range = list(range(2,1000000))

for x in in_range:
	list = []

	while x !=1 :
		if x%2 == 0:
			x = x/2
			list.append(x)
		else:
			x = (3*x + 1)
			list.append(x)
	z = len(list)
	new_list.append(z)

print(new_list)
index, value = max(enumerate(new_list), key=operator.itemgetter(1))
print(index + 2, value)