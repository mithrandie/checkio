import math


def degree(a, b, c):
    return round(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))


def checkio(a, b, c):
    sides = sorted([a, b, c], reverse=True)
    if sum(sides[1:]) <= sides[0]:
        return [0, 0, 0]

    return sorted([degree(a, b, c), degree(b, a, c), degree(c, a, b)])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
