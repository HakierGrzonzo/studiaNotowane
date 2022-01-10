def silnia():
    yield 1
    yield 1
    krok = 3
    wynik = 2
    while True:
        yield wynik
        wynik = wynik * krok
        krok += 1


for n in silnia():
    print(n)
