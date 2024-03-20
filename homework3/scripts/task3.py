from task1 import Matrix
import itertools

class MatrixHashMixin:
    def __hash__(self):
        hash_val = 0
        for row in self.matrix:
            for element in row:
                hash_val ^= hash(element)  # Простейшая хэш-функция - XOR всех элементов матрицы
        return hash_val

class HashedMatrix(Matrix, MatrixHashMixin):
    _cache = {}

    def __matmul__(self, other):
        key = tuple([sum(list(itertools.chain(*self.matrix))) + hash(other), sum(list(itertools.chain(*other.matrix))) + hash(self)])
        if key in HashedMatrix._cache:
            return HashedMatrix._cache[key]
        result = Matrix(super().__matmul__(other).matrix)
        HashedMatrix._cache[key] = result
        return result

if __name__ == "__main__":
    import numpy as np

    A = HashedMatrix([[1, 1], [3, 4]])
    B = HashedMatrix([[1, 2], [2, 1]])
    C = HashedMatrix([[0, 0], [3, 4]])
    D = HashedMatrix([[1, 2], [2, 1]])

    assert hash(A) == hash(C)
    assert A.matrix != C.matrix
    assert B.matrix == D.matrix

    a_mul_b = A @ B
    c_mul_d = C @ D
    assert a_mul_b.matrix != c_mul_d.matrix

    np.savetxt('../artifacts/3_3/A.txt', A.matrix, fmt='%s')
    np.savetxt('../artifacts/3_3/B.txt', B.matrix, fmt='%s')
    np.savetxt('../artifacts/3_3/C.txt', C.matrix, fmt='%s')
    np.savetxt('../artifacts/3_3/D.txt', D.matrix, fmt='%s')
    np.savetxt('../artifacts/3_3/AB.txt', a_mul_b.matrix, fmt='%s')
    np.savetxt('../artifacts/3_3/CD.txt', c_mul_d.matrix, fmt='%s')

    with open('../artifacts/3_3/hash.txt', 'w') as file:
        file.writelines(f'AB hash: {hash(a_mul_b)}\n')
        file.writelines(f'CD hash: {hash(c_mul_d)}\n')
