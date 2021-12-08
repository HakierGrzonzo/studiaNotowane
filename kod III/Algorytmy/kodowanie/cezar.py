def cezar(source: str, offset: int):
    return bytes(
            [(x + offset) % 255 for x in source.encode(errors='ignore')]
        ).decode(errors='ignore')

print(cezar("abc", 1))
print(cezar(cezar("politechnika", 3), -3))
