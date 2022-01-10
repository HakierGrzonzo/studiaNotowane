def getDataGenerator():
    while True:
        data = getOneData()
        if data is None:
            # no data left to process
            break
        yield processData(data)


def gatherUserActions(data):
    for datapoint in data:
        if askUserForAction(datapoint):
            yield datapoint


def main():
    saveData(
        gatherUserActions(getDataGenerator())
    )
