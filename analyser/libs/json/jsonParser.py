import json

def convertToJson(data):
    return json.dumps(data)


def convertFromJson(data):
    return json.loads(data)
