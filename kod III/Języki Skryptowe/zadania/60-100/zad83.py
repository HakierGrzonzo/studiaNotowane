def getnum() -> int:
    while True:
        try:
            return int(input("Podaj liczbę: "))
        except:
            pass

