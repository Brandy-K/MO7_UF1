numeros = input("Enter 10 numeros separats per espai: ")

myList = list(map(int, numeros.split()))

if len(myList) != 10:
    print("Enter 10 numbers!!")
else:
    suma = sum(myList)
    mitjana = suma / len(myList)
    myList.append(suma)
    myList.append(mitjana)

    print("Llista amb suma i mitjana:", myList)
    print("La suma es: ", suma)
    print("La mitjana es: ", mitjana)
