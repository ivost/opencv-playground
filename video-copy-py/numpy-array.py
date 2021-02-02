import numpy as np


class MyArray:

    def __init__(self, rows, cols, type=np.uint8):
        self._arr = np.zeros((rows, cols), type)

    def __str__(self):
        s = f'{self._arr}'
        return s

    @property
    def num_rows(self):
        return self._arr.shape[0]

    @property
    def num_cols(self):
        return self._arr.shape[1]

    @property
    def type(self):
        return self._arr.dtype


if __name__ == '__main__':
    r = 2
    c = 3
    a = MyArray(r, c)
    assert a.num_rows == r
    assert a.num_cols == c
    print(a)
    print(a.type)
