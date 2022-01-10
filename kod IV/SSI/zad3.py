objs = list(
    zip(
        [
            # pomidory
            {
                "świeże": True,
                "mrożone": False,
                "ostre": False,
                "słodkie": True,
                "zielone": False,
                "czerwone": True,
                "lokalne": True,
                "tropikalne": False,
                "liściaste": True,
                "bulwowe": False,
            },
            # pomarańcze
            {
                "świeże": True,
                "mrożone": False,
                "ostre": False,
                "słodkie": False,
                "zielone": False,
                "czerwone": True,
                "lokalne": False,
                "tropikalne": True,
                "liściaste": True,
                "bulwowe": False,
            },
            # ogórki
            {
                "świeże": False,
                "mrożone": False,
                "ostre": False,
                "słodkie": False,
                "zielone": True,
                "czerwone": False,
                "lokalne": True,
                "tropikalne": False,
                "liściaste": False,
                "bulwowe": True,
            },
            # czosnek
            {
                "świeże": True,
                "mrożone": False,
                "ostre": True,
                "słodkie": False,
                "zielone": False,
                "czerwone": False,
                "lokalne": True,
                "tropikalne": False,
                "liściaste": False,
                "bulwowe": True,
            },
            # papryka
            {
                "świeże": False,
                "mrożone": True,
                "ostre": True,
                "słodkie": False,
                "zielone": False,
                "czerwone": True,
                "lokalne": False,
                "tropikalne": False,
                "liściaste": True,
                "bulwowe": False,
            },
            {
                "świeże": False,
                "mrożone": True,
                "ostre": True,
                "słodkie": False,
                "zielone": False,
                "czerwone": True,
                "lokalne": False,
                "tropikalne": False,
                "liściaste": True,
                "bulwowe": False,
            },
        ],
        ["pomidory", "pomarańcze", "ogórki", "czosnek", "papryka", "papryka"],
    )
)
a = {"świeże": 1, "ostre": 0.2, "czerwone": 1}
b = {"mrożone": 1, "zielone": 0.2, "słodkie": 0.2, "liściaste": 0.2}
c = {"świeże": 1, "zielone": 0.1, "czerwone": 0.3, "słodkie": 1}


def classify(objs, reqs):
    res = list(
        (label, sum(w[req] * reqs[req] for req in w if req in reqs))
        for w, label in objs
    )
    return list(label for label, w in res if w == max(w for _, w in res))


print(classify(objs.copy(), a))
print(classify(objs.copy(), b))
print(classify(objs.copy(), c))
