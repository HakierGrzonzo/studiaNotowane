def getDataGenerator():
    while True:
        data = getOneData()
        if data is None:
            # no data left to process
            break
        # return data from generator
        yield processData(data)


def main():
    result = []

    for datapoint in getDataGenerator():
        if askUserForAction(datapoint):
            result.append(datapoint)

    saveData(result)
