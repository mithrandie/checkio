import numpy


def checkio(number):
    return numpy.prod([float(i) for i in str(number) if 0 < int(i)], dtype=numpy.int32).item(0)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
