import numpy as np
import hashlib

class MatrixHashMixin:
    def __hash__(self):
        # Вычисляем хэш матрицы на основе суммы элементов
        hash_sum = np.sum(self.data)
        # Преобразуем хэш в строку и берем 4 первых символа
        hash_str = str(hash_sum)
        return int(hashlib.sha256(hash_str.encode()).hexdigest()[:4], 16)

class Matrix(MatrixHashMixin):
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

# Генерируем матрицы
np.random.seed(0)
A = np.random.randint(0, 10, (3, 3))
B = np.random.randint(0, 10, (3, 3))
C = np.random.randint(0, 10, (3, 3))
D = B.copy()  # Создаем D, чтобы B == D

# Сохраняем матрицы в файлы
np.savetxt("A.txt", A, fmt='%d')
np.savetxt("B.txt", B, fmt='%d')
np.savetxt("C.txt", C, fmt='%d')
np.savetxt("D.txt", D, fmt='%d')

# Производим операции
AB = A @ B
CD = C @ D

# Сохраняем результаты произведений в файлы
np.savetxt("AB.txt", AB, fmt='%d')
np.savetxt("CD.txt", CD, fmt='%d')

# Сохраняем хэши результатов в файл
hash_AB = hash(AB.tobytes())
hash_CD = hash(CD.tobytes())
with open("hash.txt", "w") as f:
    f.write(f"AB hash: {hash_AB}\n")
    f.write(f"CD hash: {hash_CD}\n")

print("That's all")