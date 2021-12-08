def silnia(i):
    if i > 0:
        return silnia(i - 1) * i
    return 1
print(silnia(int(input())))
