from collections import defaultdict

def boyer_moor(source: str, to_find: str):
    pom = defaultdict(lambda: -1)
    for x in set(to_find):
        pom[x] = to_find.rindex(x)
    i = len(to_find) - 1
    j = len(to_find) - 1
    while i < len(source):
        if source[i] == to_find[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            i = i + len(to_find) - min(j, 1 + pom[source[i]])
            j = len(to_find) - 1
    return -1

if __name__ == "__main__":
    print(boyer_moor("cyberpapaj 2137", "papaj"))

