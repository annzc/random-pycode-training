alph = "abcdefghijklmnopqrstuvwxyz"

msg = input().lower()
for i in msg:
    if i == " ":
        print(" ", end="")
    else:
        print(alph[-(alph.index(i)+1)], end="")
