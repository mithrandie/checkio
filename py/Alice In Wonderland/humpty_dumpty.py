#!/usr/bin/env checkio --domain=py run humpty-dumpty

# https://py.checkio.org/mission/humpty-dumpty/

# .story.shadow {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;    }
# END_DESC

def checkio(height, width):
    return [1, 1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"