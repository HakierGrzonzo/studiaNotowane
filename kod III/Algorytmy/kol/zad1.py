alfa = "abcdefghijklmnoprstuwxyz"
alfa += alfa.upper()
alfa += ",.0123456789 #"

def get_alphabet_pos(a):
    try:
        return alfa.index(a)
    except:
        return 2

def hash_func(vec):
    sum = 0
    for i, x in enumerate(vec):
        sum += get_alphabet_pos(x) * pow(len(alfa), len(vec) - i - 1)
    return sum % 23

def append_hash(prev, new, old):
    return ((prev - get_alphabet_pos(old) * pow(len(alfa), 2)) * len(alfa) + \
            get_alphabet_pos(new) ) % 23

def karp_rabin(source: str, pattern: str) -> int:
    search = hash_func(pattern)
    h = hash_func(source[:len(pattern)])
    i = 0
    res = 0
    while i < len(source) - len(pattern):
        if search == h:
            if pattern == source[i : i + len(pattern)]:
                # Sprawdzaj czy hash nas nie zawiódł
                res += 1
        h = append_hash(h, source[i + len(pattern)], source[i])
        i += 1
    return res

if __name__ == "__main__":
    print(karp_rabin("Kot się schował za kotarą", "kot"))

