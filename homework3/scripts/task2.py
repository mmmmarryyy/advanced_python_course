import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

class MyMatrixMixin:
    def __init__(self, matrix):
        self.matrix = matrix

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        if not isinstance(value, np.ndarray) and not (isinstance(value, list) and isinstance(value[0], list)):
            raise ValueError("Unsupported type, np.ndarray or list[list] expected")
        self._matrix = value

    def to_file(self, filename):
        np.savetxt(filename, self.matrix, fmt='%s')

    def __str__(self):
        return '\n'.join([' '.join(str(cell) for cell in row) for row in self._matrix])

class Matrix(NDArrayOperatorsMixin, MyMatrixMixin):
    _HANDLED_TYPES = (np.ndarray, list)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (Matrix,)):
                return NotImplemented
        inputs = list(x._matrix if isinstance(x, Matrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = list(
                x._matrix if isinstance(x, Matrix) else x
                for x in out)

        if method == '__call__':
            return Matrix(np.asarray(getattr(ufunc, method)(*inputs, **kwargs)).tolist())
        else:
            return NotImplemented


if __name__ == "__main__":
    np.random.seed(0)
    matrix1 = np.random.randint(1, 10, (10, 10))
    matrix2 = np.random.randint(1, 10, (10, 10))

    custom_matrix1 = Matrix(matrix1.tolist())
    custom_matrix2 = Matrix(matrix2.tolist())

    result_add = custom_matrix1 + custom_matrix2
    result_sub = custom_matrix1 - custom_matrix2
    result_mul = custom_matrix1 * custom_matrix2
    result_div = custom_matrix1 / custom_matrix2
    result_proc = custom_matrix1 % custom_matrix2

    assert result_add.matrix == (matrix1 + matrix2).tolist()
    assert result_mul.matrix == (matrix1 * matrix2).tolist()
    assert result_sub.matrix == (matrix1 - matrix2).tolist()
    assert result_div.matrix == (matrix1 / matrix2).tolist()
    assert result_proc.matrix == (matrix1 % matrix2).tolist()

    result_add.to_file('../artifacts/3_2/matrix+.txt')
    result_sub.to_file('../artifacts/3_2/matrix-.txt')
    result_mul.to_file('../artifacts/3_2/matrix*.txt')
    result_div.to_file('../artifacts/3_2/matrix_div.txt')
    result_proc.to_file('../artifacts/3_2/matrix%.txt')
