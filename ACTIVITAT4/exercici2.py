import numpy as np

matrix = np.array([88, 23, 39, 41])
new_mat = np.array_split(matrix, 1)

# mostrar el matriu, el size, els dimensions, el shape i tipus de data
print("Array:\n", new_mat)
print("Total number of elements:", matrix.size)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.shape)
print("Data type:", matrix.dtype)

matrix2 = np.array([[76.4, 21.7, 38.4], [41.2, 52.8, 68.9]])
new_matrix = matrix2.reshape(6, )
print("Array:\n", new_matrix)
print("Total number of elements:", new_matrix.size)
print("Dimensions:", new_matrix.ndim)
print("Size:", new_matrix.shape)
print("Data type:", new_matrix.dtype)

matrix3 = np.array([12, 4, 9, 8])
nova_matrix = matrix3.reshape(-1, 1)  # To reshape the matrix vertically
print("Array:\n", nova_matrix)
print("Total number of elements:", nova_matrix.size)
print("Dimensions:", nova_matrix.ndim)
print("Size:", nova_matrix.shape)
print("Data type:", nova_matrix.dtype)



