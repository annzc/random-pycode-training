values = ["struct","shop","part","rat","steep","cat","tap"]
for value in values:
    if len(value)>3:
        char = value[len(value)-2]
        print(char, end="")
    else:
        char = value[0]
        print(char, end="")
print()
