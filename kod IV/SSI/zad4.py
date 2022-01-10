import pandas
import random
import numpy

df = pandas.read_csv("/home/hakiergrzonzo/Downloads/iris.csv")

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

train, test = ProcessingData.split(ProcessingData.normalize(ProcessingData.shuffle(df)), .7)

means = train.groupby(["variety"]).mean()
vari = train.groupby(['variety']).var()
prior = (train.groupby(['variety']).count() / len(train)).iloc[:,1]
classes = numpy.unique(train["variety"].tolist())

def normal(n, mu, var):
    sd = numpy.sqrt(var)
    return (numpy.e ** (-0.5 * ((n - mu) / sd) ** 2 )) / (sd * numpy.sqrt(2 * numpy.pi))


def predict(x):
    res = []
    for i in x.index:
        classProb = []
        instance = x.loc[i]
        for cls in classes:
            featureProb = [numpy.log(prior[cls])]
            for col in x.columns:
                if col == "variety":
                    continue
                data = instance[col]
                mean = means[col].loc[cls]
                var = vari[col].loc[cls]
                prob = normal(data, mean, var)
                if prob != 0:
                    prob = numpy.log(prob)
                else:
                    prob = 1 / len(train)
                featureProb.append(prob)
            classProb.append(sum(featureProb))
        maxIndex = classProb.index(max(classProb))
        res.append(classes[maxIndex])
    return res

def getAcc(data, func):
    score = sum(1 for actual, pred in zip(data['variety'], func(data)) if actual == pred)
    return score / len(data['variety']) * 100

print(getAcc(train, predict), sep="\n---\n")
print(getAcc(test, predict), sep="\n---\n")

