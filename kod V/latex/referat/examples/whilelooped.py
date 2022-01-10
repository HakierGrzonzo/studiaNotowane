def main():
    result = []
    while True:
        data = getOneData()
        if data is None:
            # no data left to process
            break

        processed_data = processData(data)

        if askUserForAction(processed_data):
            result.append(datapoint)

    saveData(result)
