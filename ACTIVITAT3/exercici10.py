import string

alphabets = list(string.ascii_lowercase)  #to store alphabets

nova_llista = []  #Llista para gaurdar les lletres que no estan en la position multiples de 3

for i in range(len(alphabets)):
    if (i + 1) % 3 != 0:
        nova_llista.append(alphabets[i])

alphabets_tuple = tuple(nova_llista)  #convert them into a tupla
print("Llista sense lletres en posicions multiples de 3:", nova_llista)
print("Tupla de la llista :", alphabets_tuple)
