class Ex():
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value * other.value - 5

y = Ex(5)
print(y)
x = Ex(17)
print(x)
z = y + x
print(z+z)
