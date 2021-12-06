a = list(range(10))
b = list([str(x) if x > 6 else x for x in a])
print(*[x == y for x, y in zip(a, b)])

