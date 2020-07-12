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


def generate_transformation(cycle, offset, function=lambda x: x):
    n = len(cycle)
    return {cycle[i]: function(cycle[(i - offset) % n]) for i in range(n)}


def combine_transformations(A, B, combination, retrieve=lambda x: x[0]):
    A: dict
    B: dict
    changed = set(A.keys()) | set(B.keys())
    new = dict()
    for e in changed:
        if e in B:
            e2 = retrieve(B[e])
            if e2 in A:
                new[e] = combination(A[e2], B[e])
            else:
                new[e] = B[e]
        else:
            new[e] = A[e]


if __name__ == "__main__":
    _n = 2345
    X = decompress(_n, 5)
    Y = (X + [0 for i in range(20)])[:12]
    m = compress(Y[:], 5)
    print(_n, X, Y, m)
