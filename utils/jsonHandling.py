import json


def jsonHandling(filePath):
    with open(filePath) as data:
            finalData = json.load(data)
            print(finalData)
            return finalData