def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial (x - 1)

y = int(input("factorial : "))
result = str(factorial(y))

count_zero = 0
for i in result:
    if i == "0":
        count_zero += 1

print(count_zero)
