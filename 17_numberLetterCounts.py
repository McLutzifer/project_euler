one_to_nine = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten = ['ten']
exceptions = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
decades = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundred = 'hundred'

## 1-20
onetotwenty = one_to_nine + ten + exceptions

# starting at 20

enum = onetotwenty

# numbers from 20 to 99
def twenty_to_ninenine (ones, tens, hundreds = 0):
    for dec in tens:
        for num in ones:
            x = dec + num
            enum.append(x)

twenty_to_ninenine (one_to_nine, decades)


print(len(enum))

print(type(enum[8]))

testlist = []

#enum = 1 - 99
one_to_hundred = enum

for x in range(1, len(one_to_nine)):
    for y in one_to_hundred:
        z = one_to_nine[x] + 'hundredand' + y
        testlist.append(z)

print(len(testlist))

summe = one_to_hundred + testlist
print(len(summe))

length = []

for x in summe:
    g = len(x)
    length.append(g)

ergebn = sum(length)

result = ergebn - 16 #weil 9 mal 'and' zu oft drin und einmal onethousand zu wenig

print(result)


###########################  21124
