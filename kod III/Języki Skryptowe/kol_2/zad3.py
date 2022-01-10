def get_fibo():
    i1 = 1
    i2 = 0
    while True:
        yield i1 + i2
        tmp = i2
        i2 = i1 + i2
        i1 = tmp

if __name__ == "__main__":
    fibo = get_fibo()
    for x in range(100):
        print(fibo.__next__())
    import antigravity
