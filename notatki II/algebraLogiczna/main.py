alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"

def doubleChar2num(chars):
    chars = chars.upper()
    return alfabet.index(chars[0]) * len(alfabet) + alfabet.index(chars[1])

def rsaCipher(clearNumber, n, e):
    return pow(clearNumber, e, n)

def num2string(num):
    res = alfabet[num % len(alfabet)]
    num = int(num / 32)
    res += alfabet[num % len(alfabet)]
    num = int(num / 32)
    res += alfabet[num % len(alfabet)]
    return res[::-1]

def cipher(clearText):
    clearNumber = doubleChar2num(clearText)
    cipherNumber = rsaCipher(clearNumber, 3901, 1977)
    return num2string(cipherNumber)

def bruteforce(n, e):
    texts = ["GK", "KK", "KÓ", "DE", "BI", "LE", "ZA", "JE", "BI", "EM"]
    testpoints = [
            {
                "clear": doubleChar2num(text),
                "cipher": rsaCipher(doubleChar2num(text), n, e)
            }            
        for text in texts
    ]
    d = 1
    while True:
        if all([
                pow(test["cipher"], d, n) == test["clear"]
            for test in testpoints]):
            print("found it")
            break
        else:
            d +=1
    return d
        

if __name__ == "__main__":
    print(bruteforce(3901, 1977))
    print(cipher("MF"))
