import math


my_list = list(range(1,101))
print(list(my_list))


sum_of_squares = sum(i**2 for i in my_list)
print(sum_of_squares)

squares = sum(j for j in my_list)
squares_of_sum = squares**2

print(squares_of_sum)

print('The difference is ', squares_of_sum - sum_of_squares )