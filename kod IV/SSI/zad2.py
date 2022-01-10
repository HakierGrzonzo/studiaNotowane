import pandas

df = pandas.read_csv("/home/hakiergrzonzo/Downloads/iris.csv")

import random


class ProcessingData:
    @staticmethod
    def shuffle(data):
        for i in reversed(range(len(data))):
            j = random.randint(0, i)
            data.iloc[i], data.iloc[j] = data.iloc[j], data.iloc[i]
        return data

    @staticmethod
    def split(data, fraction):
        index = int(len(data) * fraction)
        return data[:index], data[index:]

    @staticmethod
    def normalize(data):
        values = data.select_dtypes(exclude=["object"])
        for col in values.columns.tolist():
            d = data.loc[:, col]
            d_max = d.max()
            d_min = d.min()
            for i in range(len(data)):
                data.at[i, col] = (data.at[i, col] - d_min) / (d_max - d_min)
        return data


def minkowski(p1, p2, f):
    res = 0
    for i in range(len(p1) - 1):
        res += abs(p1[i] - p2[i]) ** f
    return res ** (1 / f)


def clusters(s, data, k, f):
    classes = {x: 0 for x in data["variety"].unique()}
    distances = [minkowski(s, col, f) for col in data.iloc]
    data = data.assign(dist=distances).sort_values(by=["dist"]).drop(["dist"], axis=1)
    for i in range(k):
        classes[data.iloc[i].variety] += 1
    return max(classes, key=classes.get)

def get_accuracy(test, train, k, f):
    correct = 0
    for i in test.iloc:
        if clusters(i, train, 3, 2) == i.variety:
            correct += 1
    return f"{round(correct / len(test), 2) * 100}%"

train, test = ProcessingData.split(ProcessingData.shuffle(df), .7)
print(get_accuracy(test, train, 3, 2))
