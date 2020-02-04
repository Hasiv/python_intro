def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(50)
print(f(0))
print(f(100))
