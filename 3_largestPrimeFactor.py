pruefung = 0

# Ausgangszahl
n = 600851475143

if n <= 1:
    print ("Die von Ihnen eingegebene Zahl",  n,  "ist keine Primzahl.")

for i in range (2,  n):

    if n%i == 0:
        n = n/i
        print(i, "is i")
        print(n, "is n")

