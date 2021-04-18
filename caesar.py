# this is my version of caesar cipher
# created using my minimum knowledge :v

import random

low = " abcdefghijklmnopqrstuvwxyz"
upp = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
rand = "%\\|=[<>{@#\$\_&-+(*:;!?£¢€¥%©®¥π√÷×∆✓™)}]"

def caesar_cipher(text, seq):
    for i in text:
        if i == " ":
            print(" ", end="")
        elif i in num:
            print(num.index(i)+seq)
        elif not(i) in low + upp:
            print(random.choice(rand), end='')
        elif i == i.lower():
            idx = low.index(i) + seq
            while idx > 26:
                idx -= 26
            print(low[idx], end="")
        else:
            idx = upp.index(i) + seq
            while idx > 26:
                idx -= 26
            print(upp[idx], end="")

text = input("Enter your message : ")
while True:
    seq = input("Enter sequence : ")
    if not(seq) in num:
        print("[!] aww sorry, but that should be a number :)")
    else:
        seq = int(seq)
        break

print('\nYour secret message :\n" ', end='')
caesar_cipher(text, seq)
print(' "')
