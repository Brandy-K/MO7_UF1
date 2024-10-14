import numpy as np

matrix = np.diag(np.arange(50))

np.save('exercici1.npy', matrix)


print("Matrix:\n", matrix)
print("Dimensions:", matrix.ndim)
print("El tamany de matriu:", matrix.shape)
print("Numero delements total:", matrix.size)
print("Data type:", matrix.dtype)

'''matrix = np.diag(np.arange(49).reshape(7, 7))
print("Matrix:\n", matrix)'''
