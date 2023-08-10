def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nww(c, d):
    result = (c * d) / nwd(c, d)
    return result


print(nww(8, 20))
