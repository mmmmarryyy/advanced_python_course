class Matrix:
    def __init__(self, matrix):
        for i in range(1, len(matrix)):
            if len(matrix[i-1]) != len(matrix[i]):
                raise ValueError("It's not a matrix")
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must be of the same shape")
        
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must be of the same shape")
        
        result = [[self.matrix[i][j] * other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def __matmul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Number of columns in the first matrix must match number of rows in the second matrix for matrix multiplication")
        
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix))) for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

if __name__ == "__main__":
    import numpy as np
    np.random.seed(0)
    matrix1 = np.random.randint(0, 10, (10, 10))
    matrix2 = np.random.randint(0, 10, (10, 10))

    matrix_obj1 = Matrix(matrix1.tolist())
    matrix_obj2 = Matrix(matrix2.tolist())

    result_add = matrix_obj1 + matrix_obj2
    result_mul = matrix_obj1 * matrix_obj2
    result_matmul = matrix_obj1 @ matrix_obj2

    assert result_add.matrix == (matrix1 + matrix2).tolist()
    assert result_mul.matrix == (matrix1 * matrix2).tolist()
    assert result_matmul.matrix == (matrix1 @ matrix2).tolist()

    np.savetxt('../artifacts/3_1/matrix+.txt', result_add.matrix, fmt='%s')
    np.savetxt('../artifacts/3_1/matrix*.txt', result_mul.matrix, fmt='%s')
    np.savetxt('../artifacts/3_1/matrix@.txt', result_matmul.matrix, fmt='%s')