alph = "abcdefghijklmnopqrstuvwxyz"
back_alph = {a:b for (a,b) in zip(alph,alph[::-1])}

msg = input().lower()
for i in msg:
    if i == " ":
        print(" ", end="")
    else:
        print(back_alph[i], end="")
