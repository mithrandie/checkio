import string


def checkio(text):
    letters = [l for l in text.lower() if l in string.ascii_lowercase]
    counts = {k: letters.count(k) for k in set(letters)}
    max_count = max(counts.values())
    max_letters = sorted([k for k, v in counts.items() if v == max_count])
    return max_letters[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
