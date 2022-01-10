def tobase12(n: int) -> str:
    if n == 0:
        return '0'

    base = "0123456789AB"
    res = ""
    if n < 0:
        res += "-"
        n = abs(n)
    while n > 0:
        res = base[n % 12] + res
        n //= 12 
    return res

def tobase3(n: int) -> str:
    if n == 0:
        return '0'
    base = "012"
    res = ""
    if n < 0:
        res += "-"
        n = abs(n)
    while n > 0:
        res = base[n % 3] + res
        n //= 3 
    return res

def frombase12(s: str) -> int:
    s = s.strip()
    res = 0
    for x in s:
        res = res * 12 + "0123456789AB".index(x)
    return res

def frombase3(s: str) -> int:
    s = s.strip()
    res = 0
    for x in s:
        res = res * 3 + "012".index(x)
    return res

with open("danezadanie1.txt") as infile:  
    with open("wyjściezad2.txt", "w+") as out:
        def printFile(*args):
            print(*[("{:" + form + "20}").format(x) for x, form in zip(args, "<^>")], sep=" | ", file=out)
        printFile("Liczby dziesiętne", "liczby trójkowe", "liczby dwunastkowe")
        print("-" * 67, file=out)
        for n in infile:
            try:
                if n.startswith("0x"):
                    num = frombase3(n.removeprefix("0x"))
                else:
                    num = int(n)
            except ValueError:
                num = frombase12(n)
            printFile(num, tobase3(num), tobase12(num))


