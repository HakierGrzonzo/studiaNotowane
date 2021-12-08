def naiwny(source:str, toFind: str) -> int:
    for i in range(0, len(source) - len(toFind)):
        for j in range(0, len(toFind)):
            if source[i + j] != toFind[j]:
                break
        else:
            return i
    return -1

if __name__ == "__main__":
    print(naiwny("jestem studentem", "stu"))

