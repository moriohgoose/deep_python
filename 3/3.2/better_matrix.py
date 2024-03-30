import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

class FileHandlerMixin:
    def write_to_file(self, filename):
        print("Запись в файл", filename)
        with open(filename, 'w') as file:
            file.write(str(self))

class DisplayMixin:
    def __str__(self):
        return str(self.data)

class GetterSetterMixin:
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value

class CustomMatrix(FileHandlerMixin, DisplayMixin, GetterSetterMixin, NDArrayOperatorsMixin):
    def __init__(self, data):
        self.data = np.array(data)

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must have the same shape for addition")
        return CustomMatrix(self.data + other.data)
    
    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must have the same shape for element-wise multiplication")
        return CustomMatrix(self.data * other.data)
    
    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for matrix multiplication")
        return CustomMatrix(np.matmul(self.data, other.data))


# Генерация матриц
np.random.seed(0)
matrix1 = np.random.randint(0, 10, (3, 3))
matrix2 = np.random.randint(0, 10, (3, 3))

# Создание экземпляров класса CustomMatrix
custom_matrix1 = CustomMatrix(matrix1)
custom_matrix2 = CustomMatrix(matrix2)

try:
    addition_result = custom_matrix1 + custom_matrix2
    multiplication_result = custom_matrix1 * custom_matrix2
    matrix_multiplication_result = custom_matrix1 @ custom_matrix2
except ValueError as e:
    print("Error during operation:", e)

# Запись результатов в файлы
addition_result.write_to_file("matrix+.txt")
multiplication_result.write_to_file("multiplication_result.txt")
matrix_multiplication_result.write_to_file("matrix@.txt")


