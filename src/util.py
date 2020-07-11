def identitylist(size):
    return [(i, 0) for i in range(size)]


def compress(values, size):
    n = 0
    while len(values) > 0:
        n <<= size
        n += values.pop()
    return n


def decompress(n, size):
    values = list()
    while n > 0:
        values.append(n % (1 << size))
        n >>= size
    return values


def transformation(cycle, offset):
    n = len(cycle)
    return {cycle[i]: cycle[(i - offset) % n] for i in range(n)}


if __name__ == "__main__":
    _n = 2345
    X = decompress(_n, 5)
    Y = (X + [0 for i in range(20)])[:12]
    m = compress(Y[:], 5)
    print(_n, X, Y, m)
