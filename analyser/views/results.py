from analyser.libs.json.jsonView import JSONView
from analyser.libs.phisics.matrix import fullMatrix
from analyser.libs.phisics.misalignments import newAxisRotated, calculateDeltas
from analyser.libs.helpful.converters import convertArray
from analyser.views.paramsTransformation import DATA_NAMES, DATA_IN_ARRAY
import numpy

from django.http import HttpResponse


ARRAY_NAME = 'deltas'

def getNum(data):
    return len(data.values()[0])

def dictConversion(data):
    converted = {}
    for (key, value) in DATA_NAMES.items():
        converted[value] = convertArray(data[key])
    return converted


def arrayConversion(data):
    converted = []

    for key in DATA_IN_ARRAY:
        converted.append(convertArray(data[key]))

    return numpy.transpose(converted)


def getResult(data, calc, converter=dictConversion):

    results = []
    converted = converter(data)

    for i in range(getNum(data)):
        converted['n'] = i
        calculated = calc(**converted).tolist()
        results.append(calculated)

    return results


class MatrixView(JSONView):
    def handleGet(self, data):
        return getResult(data, fullMatrix)


class MisView(JSONView):

    def getDeltas(self, data, parameters):

        misalignments = arrayConversion(data)
        angles = parameters['angleArray']
        radiusArray = parameters['radiusArray']
        return calculateDeltas(misalignments, angles, radiusArray)

    def handleGet(self, data):

        parameters = dictConversion(data)
        parameters[ARRAY_NAME] = self.getDeltas(data, parameters)

        try:
            result = getResult(parameters, newAxisRotated, lambda a: a)

        except numpy.linalg.LinAlgError:
            return 'singular matrix'

        return result