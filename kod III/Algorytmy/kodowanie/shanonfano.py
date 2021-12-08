def shannon(string: str):
    symbols = [{"symbol": x, "prob": string.count(x) / len(string)} for x in set(string)]
    def do(l):
        if len(l) > 2:
            th = sum([x['prob'] for x in l])
            s = 0
            for i, x in enumerate(l):
                s += x['prob']
                if s > th / 2 and i != 0:
                    left = do(l[:i])
                    right = do(l[i:])
                    res = dict()
                    for k, v in left.items():
                        res[k] = "0" + v
                    for k, v in right.items():
                        res[k] = "1" + v
                    return res
            else:
                raise Exception()

        elif len(l) == 1:
            return {l[0]['symbol']: ""}
        elif len(l) == 2:
            return {l[0]['symbol']: "0", l[1]['symbol']: "1"}
        else:
            raise Exception()
    return do(symbols)



if __name__ == "__main__":
    print(shannon("hewwo"))
    print(shannon("to be or not to be"))
    print(shannon("Did I ever tell you the definition of insanity? Insanity is doing the same thing over and over again, and expecting things to be diffrent"))
