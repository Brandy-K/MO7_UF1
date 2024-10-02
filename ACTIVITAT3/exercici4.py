enter_numero = (input("Enter 10 numbers: "))

numeros = list(map(int, enter_numero.split()))

if len(numeros) != 10:
    print("You must enter 10 numbers!")
else:
    numero_ordenada = sorted(numeros)
    numero_ordenada_tuple = tuple(numero_ordenada)
    print(numero_ordenada_tuple)
