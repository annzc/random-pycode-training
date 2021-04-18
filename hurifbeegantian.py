s = input("input: ")
def hurufBergantian(s):
    return sum([1 for i in range(1,len(s)) if s[i] == s[i-1]])
print(hurufBergantian(s))
