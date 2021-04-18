import os

def char_count(txt, char):
    jml = 0
    for j in txt:
        if j == char:
            jml += 1
    return jml

if os.path.isfile("text.txt") == False:
    os.system("echo \"this is an example this iß an example this is an example this is an example for your information this is an example created for purpose\" > text.txt")
else:
    print("file already created √ ")

with open("textanalyzer.py") as txxt:
    f = txxt.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    persen = 100 * char_count(f, char) / len(f)
    print("{0} - {1}%".format(char, round(persen, 2)))

persen = 100 * char_count(f, char) / len(f)
print(round(persen, 2))
print(persen)
print(char_count(f, char))
