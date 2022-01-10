import pandas
df = pandas.read_csv('/home/hakiergrzonzo/Downloads/iris.csv')

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
            d = data.loc[:,col]
            d_max = d.max()
            d_min = d.min()
            for i in range(len(data)):
                data.at[i, col] = (data.at[i, col] - d_min) / (d_max - d_min)
        return data

print(ProcessingData.normalize(ProcessingData.shuffle(df)))

