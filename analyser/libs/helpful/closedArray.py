
def rotateLeft(arr, n=1):
    first = arr[n:]
    last = arr[:n]
    result = []
    result.extend(first)
    result.extend(last)
    return result


def rotateArgs(args, n):
    return [rotateLeft(i, n) for i in args]

if __name__ == '__main__':
    import numpy

    a = [1, 2, 3, 4, 5]
    print(rotateLeft(a, 1))
    print(rotateLeft(a, 2))
    print(rotateLeft(a, 0))
    print(rotateLeft(numpy.array(a), 1))
    print(rotateLeft(numpy.array(a), 2))

