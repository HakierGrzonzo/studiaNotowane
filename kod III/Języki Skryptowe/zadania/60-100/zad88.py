from random import randint
k = int(input("Podaj liczbę kolumn: "))
print("\n".join(["\t".join([str(randint(0, 16)) for _ in range(k)]) for _ in range(int(input("Podaj liczbę wierszy: ")))]))
