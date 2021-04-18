from collections import Counter
a = input("string =")
unique = True
for i in Counter(a).values():
    if i > 1:
        unique = False
    else:
        pass
if unique == True:
    print("Unique")
else:
    print("Deja Vu")
