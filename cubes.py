from itertools import product, permutations

cube = (1,2,3,4,5,6)
pos = list(product(cube, range(1,7)))
print(pos)
print(len(pos))

lisumpos = [i[0]+i[1] for i in pos]

print("sumpos:",lisumpos)
print("angka terbesar:",max(lisumpos))
print("angka terkecil:",min(lisumpos))

lisum = [i for i in range(min(lisumpos),(max(lisumpos)+1))]

print("=======")
print(lisum)
print("=======")

def cnt(x, y):
    c = 0
    for i in x:
        if i in y:
            c += 1
    print(c)









print("========================")
sumcube = list(permutations(cube))
print("total: ",len(sumcube))
