import numpy


def checkio(game_result):
    rows = game_result
    rows.extend([''.join(c) for c in zip(*game_result)])
    rows.append(''.join(numpy.diag([list(r) for r in game_result])))
    rows.append(''.join(numpy.diag([list(reversed(r)) for r in game_result])))

    return 'X' if 'XXX' in rows else 'O' if 'OOO' in rows else 'D'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

