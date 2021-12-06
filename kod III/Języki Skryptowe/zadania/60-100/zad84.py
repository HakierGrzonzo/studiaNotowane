def getnum():
    while True:
        try:
            n = input()
            return (int(n), True) if int(n.replace(".", "")) == float(n) else (float(n), False)
        except:
            pass
print(getnum())
