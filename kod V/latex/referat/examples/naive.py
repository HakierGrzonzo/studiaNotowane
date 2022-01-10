def main():
    data = getAllData()

    processed_data = []
    for rawData in data:
        processed_data.append(processData(rawData))

    result = []
    for datapoint in processed_data:
        if askUserForAction(datapoint):
            result.append(datapoint)

    saveData(result)
