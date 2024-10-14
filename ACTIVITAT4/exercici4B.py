import numpy as np

matrix = np.random.randint(0, 81, size=(4, 3))
print("El Matrix original:\n", matrix)

# agafa la ultima fila
last_row = matrix[-1, :]

matrix = matrix[:-1, :]  # para treure la ultima fila del matrix

last_row_as_column = last_row.reshape(3, 1)  # reshape the matrix

# Append la ultima fila com la nueva columna
new_matrix = np.append(matrix, last_row_as_column, axis=1)

print("\nNew Matrix with last row as the last column:\n", new_matrix)




