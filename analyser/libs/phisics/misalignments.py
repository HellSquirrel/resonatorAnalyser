from analyser.libs.phisics.matrix import *
from numpy import eye, zeros, dot, array
from numpy.linalg import inv
from analyser.libs.helpful import closedArray
from matrix import incidenceAngle

#Todo: not working (
def newAxis(pathArray, angleArray, radiusArray, deltas):

    m1 = inv(eye(DIM, DIM)-fullMatrix(pathArray, angleArray, radiusArray))

    m2 = zeros(DIM)
    for i in range(len(pathArray)):
        m2 += matrixProduct([domainMatrixProduct(pathArray, angleArray, radiusArray, i + 1),
                             partialDomainMatrix(pathArray[i], angleArray[i]),
                             deltas[i]])
    return dot(m1, m2)


def newAxisRotated(pathArray, angleArray, radiusArray, deltas, n=0):
    args = closedArray.rotateArgs((pathArray, angleArray, radiusArray, deltas), n)
    return newAxis(*args)



def calculateDeltas(misalingnments, angleArray, radiusArray):
    deltas = []
    for mis, angle, radius in zip(misalingnments, angleArray, radiusArray):
        ia = incidenceAngle(angle)
        deltas.append(dot(misalignmentMatrix(ia, radius), mis))

    return deltas

if __name__ == '__main__':
    from numpy import pi
    deltas = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0.001, 0, 0],
              [0, 0, 0, 0, 0]]



    pathArray = [0.2 / 4, 0.2 / 4, 0.2 / 4, 0.2 / 4]
    angleArray = [pi / 8, -pi / 8, pi / 8, -pi / 8]
    radiusArray = ["Infinity", "Infinity", 3.6, "Infinity"]
    calculated = calculateDeltas(deltas, angleArray, radiusArray)
    print(calculated)
    na = newAxisRotated(pathArray, angleArray, radiusArray, calculated)
    na1 = newAxisRotated(pathArray,angleArray, radiusArray, calculated, 1)
    na2 = newAxisRotated(pathArray,angleArray, radiusArray, calculated, 2)
    na3 = newAxisRotated(pathArray,angleArray, radiusArray, calculated, 3)
    fm = fullMatrix(pathArray, angleArray, radiusArray, 1)
    print(na)
    print(na1)
    print(na2)
    print(na3)
    print(fm)
    print(inv(eye(DIM, DIM)-fullMatrix(pathArray, angleArray, radiusArray)))
