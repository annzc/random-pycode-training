def f(x):
    x = x.lower()
    r = str()
    for i in range(len(x)):
        c = ord(x[i])
        r += chr(c+(25+(97-c)*2)) if 97 <= c <= 122 else x[i]
    return r

print(f("apakah ini bisa"))

