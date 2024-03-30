import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
    
    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must have the same shape for addition")
        return Matrix(self.data + other.data)
    
    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must have the same shape for element-wise multiplication")
        return Matrix(self.data * other.data)
    
    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for matrix multiplication")
        return Matrix(np.matmul(self.data, other.data))

    def __str__(self):
        return str(self.data)

# Генерация двух матриц через np.random.randint(0, 10, (10, 10)) c seed-ом 0
np.random.seed(0)
matrix1 = np.random.randint(0, 10, (10, 10))
matrix2 = np.random.randint(0, 10, (10, 10))

# Создание экземпляров класса Matrix
matrix1_obj = Matrix(matrix1)
matrix2_obj = Matrix(matrix2)

# Выполнение операций
try:
    addition_result = matrix1_obj + matrix2_obj
    multiplication_result = matrix1_obj * matrix2_obj
    matrix_multiplication_result = matrix1_obj @ matrix2_obj
except ValueError as e:
    print("Error during operation:", e)
else:
    # Запись результатов в файлы
    np.savetxt("matrix+.txt", addition_result.data, fmt='%d')
    np.savetxt("matrix_multiply.txt", multiplication_result.data, fmt='%d')
    np.savetxt("matrix@.txt", matrix_multiplication_result.data, fmt='%d')
