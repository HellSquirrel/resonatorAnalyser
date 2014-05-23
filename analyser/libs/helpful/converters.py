
def extendedFloat(string):
    if string == u'\u221e':
        return "Infinity"

    else:
        return float(string)


def convertArray(array):
    return map(extendedFloat, array)