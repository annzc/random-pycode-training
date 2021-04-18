renj = int(input("> "))
a, b, c = 0, 1, 0
c = a + b
for i in range(renj):
    print(c)
    a = b
    b = c
    c = a + b
