import numpy as np

matrix = np.random.randint(0, 81, size=(4, 3))
print("El Matrix original:\n", matrix)

# agafa la ultima fila
last_row = matrix[-1, :]

matrix = matrix[:-1, :]  # para treure la ultima fila del matrix

last_row_as_column = last_row.reshape(3, 1)  # reshape the matrix

# Append the last row as a new column
new_matrix = np.append(matrix, last_row_as_column, axis=1)

first_last_column_value = new_matrix[0, -1]  # el primer numero en la ultima columna

# Replace all values in the last column with the first number in the last column
new_matrix[:, -1] = first_last_column_value

print("\nEl matriu modificada:\n", new_matrix)
