import itertools as iter

strlst = ['who','am','I','?']
saikel = iter.cycle(strlst)
for i in range(20):
    print(next(saikel), end=" ")
