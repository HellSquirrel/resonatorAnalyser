from __future__ import division
from numpy import *
from analyser.libs.math.matrixOperations import matrixProduct
from analyser.libs.helpful import closedArray

DIM = 4

def incidenceAngle(rotation):
    return arctan(sqrt(cos(rotation)))


def transmitMatrix(path):
    T = eye(4, 4)
    T[0][2] = T[1][3] = path
    return T


def rotationMatrix(phi):
    return array([[cos(phi), sin(phi), 0, 0],
                  [-sin(phi), cos(phi), 0, 0],
                  [0, 0, cos(phi), sin(phi)],
                  [0, 0, -sin(phi), cos(phi)]])


def reflectionMatrix(theta, radius="Infinity"):
    plane = array([[-1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, -1, 0],
                   [0, 0, 0, 1]], dtype="float")

    if radius == "Infinity":
        return plane

    else:
        plane[2, 0] = 2/(radius*cos(theta))
        plane[3, 1] = -2*cos(theta)/radius
        return plane


def misalignmentMatrix(theta, radius='Infinity'):
    plane = array([[0, 0, 2*sin(theta), 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 2],
                   [0, 0, 0, 2*cos(theta), 0]], dtype="float")

    if radius == "Infinity":
        return plane

    else:
        plane[2, 0] = -2/radius
        plane[2, 2] = -2*tan(theta)/radius
        plane[3, 1] = -2*cos(theta)/radius
        return plane


def domainMatrix(path, angle, radius):
    return matrixProduct([transmitMatrix(path),
                          rotationMatrix(angle),
                          reflectionMatrix(incidenceAngle(angle), radius)])

def partialDomainMatrix(path, angle):
    return matrixProduct([transmitMatrix(path), rotationMatrix(angle)])


def domainMatrixProduct(pathArray, angleArray, radiusArray, start=0, stop=3):
    M = eye(DIM, DIM)
    for (path, phi, radius) in zip(pathArray[start:stop+1], angleArray[start:stop+1], radiusArray[start:stop+1]):
        M = dot(domainMatrix(path, phi, radius), M)
    return M

#calculates ray matrix between zero point and observed point
#def matrixDelta()

def fullMatrix(pathArray, angleArray, radiusArray, n=0):
    rotated = [closedArray.rotateLeft(arg, n) for arg in (pathArray, angleArray, radiusArray)]
    return domainMatrixProduct(*rotated)


if __name__ == "__main__":
    print(incidenceAngle(pi/8))
    print(transmitMatrix(0.2/4))
    print(rotationMatrix(pi/8))
    print(reflectionMatrix(incidenceAngle(pi/8), 3.6))
    print(domainMatrix(0.2/4, pi/8, 3.6))
    print('----fullMatrix-----')
    print(fullMatrix([0.2/4, 0.2/4, 0.2/4, 0.2/4], [pi/8, -pi/8, pi/8, -pi/8], ["Infinity", "Infinity", 3.6, "Infinity"]))
    print(fullMatrix([0.2/4, 0.2/4, 0.2/4, 0.2/4], [pi/8, -pi/8, pi/8, -pi/8], ["Infinity", "Infinity", 3.6, "Infinity"], 1))
    print(fullMatrix([0.2/4, 0.2/4, 0.2/4, 0.2/4], [pi/8, -pi/8, pi/8, -pi/8], ["Infinity", "Infinity", 3.6, "Infinity"], 2))
    print(fullMatrix([0.2/4, 0.2/4, 0.2/4, 0.2/4], [pi/8, -pi/8, pi/8, -pi/8], ["Infinity", "Infinity", 3.6, "Infinity"], 3))