def checkio(data):
    if len(data) < 10:
        return False

    flag = 0
    for c in data:
        if flag & 1 == 0 and c.isdigit():
            flag = flag | 1

        if flag & 2 == 0 and c.islower():
            flag = flag | 2

        if flag & 4 == 0 and c.isupper():
            flag = flag | 4

        if flag == 7:
            break

    return flag == 7


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
