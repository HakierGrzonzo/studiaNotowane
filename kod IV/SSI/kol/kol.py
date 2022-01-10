import pandas
import numpy as np

df = pandas.read_csv("BankNote_Authentication.csv")

# Analiza danych

print(df)

print(df.describe())

print(df.info())

import seaborn
# Figure-1.png
# variance jest skorelowane z klasą
#seaborn.pairplot(df, hue="class")

# Figure-2.png
#seaborn.violinplot(y="class", x="variance", data=df, inner='quartile')
import matplotlib.pyplot as plt
#plt.show()
import random


class ProcessingData:
    @staticmethod
    def ShuffleData(data):
        for i in reversed(range(len(data))):
            j = random.randint(0, i)
            data.iloc[i], data.iloc[j] = data.iloc[j], data.iloc[i]
        return data

    @staticmethod
    def SplitData(data, x, y):
        if not x + y == 100:
            raise Exception("x + y != 100")
        fraction = x / (y + x)
        index = int(len(data) * fraction)
        return data[:index], data[index:]

    @staticmethod
    def getTypeCount(data):
        """Zlicz liczbę klas w zbiorze dannych"""
        values = data.select_dtypes(exclude=["object"])
        types = set()
        for col in values.columns.tolist():
            if col != "class":
                continue
            for i in range(len(data)):
                types.add(values.at[i, col])
        return len(types)

    @staticmethod
    def normalizeData(data):
        values = data.select_dtypes(exclude=["object"])
        for col in values.columns.tolist():
            if col == "class":
                continue
            d = data.loc[:, col]
            d_max = d.max()
            d_min = d.min()
            for i in range(len(data)):
                data.at[i, col] = (data.at[i, col] - d_min) / (d_max - d_min)
        return data

    @classmethod
    def group(cls, data):
        colNames = data.columns.tolist()
        typeCount = cls.getTypeCount(data)
        countArr = {x: 0 for x in range(typeCount)}
        # Stwórz początkowy słownik słowników
        types = {
            x: {name: 0 for name in colNames if name != "class"} for x in range(typeCount)
        }
        for row in range(len(data)):
            type = data.at[row, "class"]
            # Pobierz słownik ze słownika, pass refrence by value
            typeDict = types[type]
            for i in range(len(colNames)):
                if colNames[i] == "class":
                    continue
                typeDict[colNames[i]] += data.at[row, colNames[i]]
            countArr[type] += 1
        return [
            {k: round(v / countArr[typeNum]) for k, v in type.items()}
            for typeNum, type in types.items()
        ]

# Testowanie danych nieznormalizowanych

data = ProcessingData.normalizeData(ProcessingData.ShuffleData(df))
data = ProcessingData.ShuffleData(df)

from pprint import pprint

# Testowanie proporcji

train, test = ProcessingData.SplitData(data, 60, 40)

print("Treningowy:", len(train), train, sep="\n", end="\n----\n\n")
print("Testowy:", len(test), test, sep="\n", end="\n----\n\n")

print("Tabela ważona zbioru miękkiego")
pprint(ProcessingData.group(train))
print()


class SoftClassifier:
    @staticmethod
    def classify(weights, demands):
        res = [0 for _ in range(len(weights))]
        for i in range(len(weights)):
            for trait in weights[i]:
                if trait in demands:
                    res[i] += weights[i][trait] * demands[trait]
        return res.index(max(res))


class NaiveClassifier:
    @staticmethod
    def equation(x, dev, mean):
        if x < (mean - np.sqrt(6) * dev):
            return 0
        elif mean - np.sqrt(6) * dev <= x <= mean:
            return (x - mean) / (6 * dev ** 2) + 1 / (np.sqrt(6) * dev)
        elif mean < x <= mean + np.sqrt(6) * dev:
            return -(x - mean) / (6 * dev ** 2) + 1 / (np.sqrt(6) * dev)
        return 0

    @classmethod
    def classify(cls, data, sample):
        types = [data[data['class'] == x] for x in range(1, 4)]
        res = [0 for _ in range(4)]
        for i, type in enumerate(types):
            meanlist = [np.mean(type.iloc[:, k]) for k in range(4)]
            devlist = [np.std(type.iloc[:, k]) for k in range(4)]
            gausslist = [
                cls.equation(sample.iloc[k], devlist[k], meanlist[k])
                for k in range(4)
            ]
            res[i] = np.prod(gausslist * len(type)) / len(data)
        return res.index(max(res)) + 1


class KNN:
    def __init__(self, original_set) -> None:
        self.typeCount = ProcessingData.getTypeCount(original_set)

    @staticmethod
    def metryka(a, b):
        return sum(abs(x - y) for x, y in zip(a, b))

    def clustering(self, sample, data, k):
        dists = [self.metryka(sample, data.iloc[x]) for x in range(len(data))]
        data = (
            data.assign(dist=dists)
            .sort_values(by=["dist"])
            .drop(["dist"], axis=1)
        )
        classes = {x: 0 for x in range(self.typeCount)}
        for i in range(k):
            classes[data.iloc[i]["class"]] += 1
        return max(classes, key=classes.get)


knn = KNN(data)

def getAccuracyKNN(test, train, k, func):
    return (
        sum(
            1
            for i in range(len(test))
            if func(test.iloc[i], train, k) == test.iloc[i]['class']
        )
        / len(test)
        * 100
    )

def getAccuracySoft(test, weights):
    return (
        sum(
            1
            for i in range(len(test))
            if SoftClassifier.classify(weights, test.iloc[i, :8])
            == test.iloc[i]["class"]
        )
        / len(test)
        * 100
    )


def getAccuracyNaive(data):
    return (
        sum(
            1
            for i in range(len(data))
            if NaiveClassifier.classify(data, data.iloc[i, :8])
            == data.iloc[i]["class"]
        )
        / len(data)
        * 100
    )


print("KNN:", getAccuracyKNN(test, train, 4, knn.clustering), sep="\t")
print("Klasyfikator miękki:", f"{round(getAccuracySoft(test, ProcessingData.group(data)), 2)}%", sep="\t")
print("Klasyfikator Bayesa:", f"{round(getAccuracyNaive(test), 2)}%", sep="\t")
