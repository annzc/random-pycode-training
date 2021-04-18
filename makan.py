def f(x):
    return ' '.join([i[::-1] if len(i) >= 5 else i for i in x.split()])
print(f("apa kau dengar suara angin yang berhembus di muka bumi?"))
