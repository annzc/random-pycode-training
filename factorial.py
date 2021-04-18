import math

def f(x):
    rvr = str(math.factorial(x))[::-1]
    count = 0
    for i in rvr:
        if i == "0":
            count += 1
        else:
            break
    print("=>",count)

x = int(input("num : "))
f(x)
