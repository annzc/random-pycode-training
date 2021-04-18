biner = int(input("biner: "))
def bitcount(x):
    return len([i for i in bin(x) if i == '1'])
print(bitcount(biner))
