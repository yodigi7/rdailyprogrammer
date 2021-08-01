from functools import cache, wraps
import math, time
from matrices import *


def timing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        print(time.time() - start)
        return res

    return inner


@cache
def find_matrix_sum(matrix) -> int:
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    best_result = math.inf
    for i, number in enumerate(matrix[0]):
        new_matrix = tuple(tuple(row[:i] + row[i + 1 :]) for row in matrix[1:])
        result = number + find_matrix_sum(new_matrix)
        if result < best_result:
            best_result = result
    return best_result


def test():
    start = time.time()
    assert 1099762961 == find_matrix_sum(matrix_5x5)
    print(time.time() - start)
    start = time.time()
    assert 1314605186 == find_matrix_sum(matrix_20x20)
    print(time.time() - start)
    start = time.time()
    print(find_matrix_sum(matrix_97x97))
    print(time.time() - start)


test()
