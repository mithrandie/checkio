def format_number(number, base, decimals, suffix, powers, level):
    if base**level <= abs(number) and 1 < len(powers):
        return format_number(number, base, decimals, suffix, powers[1:], level+1)

    n = number if level < 2 else number / (base ** (level - 1))
    if decimals == 0:
        f = "{:d}" + powers[0] + suffix
        return f.format(int(n))
    else:
        f = "{:." + str(decimals) + "f}" + powers[0] + suffix
        return f.format(n)


def friendly_number(number, base=1000, decimals=0, suffix='', powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    return format_number(number, base, decimals, suffix, powers, 1)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

