def f(x):
    return "valid" if len(x) == 8 and x[0] in "198" else "invalid"

p = input()
print(f(p))
