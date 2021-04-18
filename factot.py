import math
def f(x):
    res = [0]
    while x >= 5:
        res.append(math.floor(x/5))
        x = math.floor(x/5)
    return sum(res)

print(f(120))
