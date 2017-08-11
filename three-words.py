def checkio(words):
    indice = [idx for idx, word in enumerate(words.split(' ')) if word.isalpha()]

    for idx, i in enumerate(indice):
        if idx + 2 < len(indice) and i + 2 == indice[idx + 2]:
            return True

    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
