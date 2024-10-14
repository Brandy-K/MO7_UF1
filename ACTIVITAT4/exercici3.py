import numpy as np
# The user to enter the dimentions of the matrix
rows = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

# create a matrix with random numbers from 1 to 100
matrix = np.random.randint(0, 101, size=(rows, column))

print("El matriu es:\n", matrix)

reshaped_matrix = matrix.reshape(-1)

# La nova matriu redimensionada
print("Reshaped Matrix:\n", reshaped_matrix)

# Max i min values del matriu
max_val = matrix.max()
min_val = matrix.min()

print("Maximum value:", max_val)
print("Minimum value:", min_val)
