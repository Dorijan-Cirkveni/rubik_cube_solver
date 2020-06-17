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


if __name__ == "__main__":
    n=2345
    X=decompress(n,5)
    Y=(X+[0 for i in range(20)])[:12]
    m=compress(Y[:],5)
    print(n,X,Y,m)