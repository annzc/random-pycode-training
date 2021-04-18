def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

with open("obj.cpp") as o:
    file = o.read()
ch = input("masukkan huruf yang mau dihitung: ")
print(f"huruf {ch} ditemukan sebanyak", count_char(file, ch))
