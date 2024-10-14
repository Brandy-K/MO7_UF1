import numpy as np

# Step 1: Generate a random 4x3 matrix
matrix = np.random.randint(0, 81, size=(4, 3))

print("Original Matrix:\n", matrix)

last_row = matrix[-1]
new_matrix = np.append(last_row, matrix[:-1])
reshape_matrix = new_matrix.reshape(4, 3)
print(reshape_matrix)

