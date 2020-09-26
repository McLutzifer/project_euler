import pprint
import numpy

row_1 = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
row_2 = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0]
row_3 = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
row_4 = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
row_5 = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
row_6 = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
row_7 = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
row_8 = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
row_9 = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
row_10 = [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95]
row_11 = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
row_12 = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57]
row_13 = [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
row_14 = [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
row_15 = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
row_16 = [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
row_17 = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
row_18 = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
row_19 = [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
row_20 = [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]


grid = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10, row_11, row_12, row_13, row_14, row_15, row_16, row_17, row_18, row_19, row_20]


############################ ............... HORIZONTAL #########################
###########################.................X Y Z ###############################


rowmax = {}

z = 0
while (z < 20):

    start = 0
    end = 4
    #print(('for row ' + str(i+1)))
    while end <= 20:

        x =((grid[z][start:end]))
        y = numpy.prod(x)
        rowmax[y] = x
        #print('from ' + str(start) + ' to ' + str(end) + ' = ',x, 'product = ', y)
        start += 1
        end += 1
    z += 1

horizont = (max(rowmax), ' from ',rowmax[48477312])
print(horizont)

###############################...............VERTIKAL#########################
###############################................U V W ##########################

v = numpy.array(grid)
u = v.transpose()
w = u.tolist()

rowmax = {}

z = 0
while (z < 20):

    start = 0
    end = 4
    #print(('for row ' + str(i+1)))
    while end <= 20:

        x =((w[z][start:end]))
        y = numpy.prod(x)
        rowmax[y] = x
        #print('from ' + str(start) + ' to ' + str(end) + ' = ',x, 'product = ', y)
        start += 1
        end += 1
    z += 1

vert = (max(rowmax), ' from ',rowmax[51267216])
print(vert)



###############################...............DIAGONAL#########################
###############################................A B C ...  ####################


A = 0
a = 0
diag = {}
diag_list = []
while a < 17:
    while A < 17:
        for e in range (4):
            b = grid[a+e][A+e]
            print(b)
            diag_list.append(b)
            print(diag_list)
        A += 1
    a += 1

    #c = numpy.prod(b)
    #diag[c] = x
    #A += 1
    #print(diag)

diagonal_max = max(diag)
print(diagonal_max)

'''
empty = {}
liiist = []

start_hor = 0
for u in range (start_hor, start_hor+3):
    for v in range (2):
        t = grid[u][v]
        #liiist[u].append(t)



        print(t)
print(liiist)
'''

"""
colmax = {}

u = 0
while (u < 20):

    start = 0
    end = 4
    #print(('for row ' + str(i+1)))
    while end <= 20:

        v =((grid[start][u]))
        w = numpy.prod(v)
        rowmax[w] = v
        #print('from ' + str(start) + ' to ' + str(end) + ' = ',x, 'product = ', y)
        start += 1
        end += 1
    u += 1

vert = (max(colmax))#, ' from ',colmax[48477312])
print(vert)
"""

'''
d = {'key':'value'}
print(d)
# {'key': 'value'}
d['mynewkey'] = 'mynewvalue'
print(d)
# {'mynewkey': 'mynewvalue', 'key': 'value'}

'''
