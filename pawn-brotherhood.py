def safe_pawns(pawns):
    return sum([1 if chr(c-1) + r in pawns or chr(c+1) + r in pawns else 0 for c, r in [(ord(c), str(int(r)-1)) for c, r in pawns]])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
