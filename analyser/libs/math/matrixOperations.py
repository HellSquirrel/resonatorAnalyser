import numpy as np


def matrixProduct(matrixArray, shape=4):
    product = np.eye(shape, shape)
    for m in matrixArray:
        product = np.dot(product, m)
    return product


def matrixProductReversed(matrixArray, shape=4):
    product = np.eye(shape, shape)
    for m in matrixArray:
        product = np.dot(m, product)
    return product



