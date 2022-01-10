def pomocnicza_kmp(pattern: str):
    p = [0, 0]
    i = 0
    for j in range(2, len(pattern)):
        while i > 0 and pattern[i] != pattern[j - 1]:
            i = p[i]
        if pattern[i] == pattern[j - 1]:
            i += 1
            p[j] = i
    return p

def knuth_morris_pratt(source: str, to_find: str) -> int:
    p = pomocnicza_kmp(to_find)
    i = 0
    j = 0
    while i < len(source) - len(to_find) + 2:
        j = p[j - 1]
        while to_find[j] == source[i + j - 2]:
            if j + 1 == len(to_find):
                break
            j += 1
        if j + 1 == len(to_find) and to_find[j] == source[i + j - 2]:
            return i - j
        i = i + max(1, j - p[j - 1])
    return -1



if __name__ == "__main__":
    print(knuth_morris_pratt("jestem studentem", "stu"))
    print(knuth_morris_pratt("debil", "bi"))
