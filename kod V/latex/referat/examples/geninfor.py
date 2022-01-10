def generator():
    yield 1
    yield 2
    yield 3


for n in generator():
    print(n)
