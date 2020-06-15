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
