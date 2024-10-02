myTupla = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

month_number = int(input("Enter un numero entre 1 and 12 (0 to exit): "))

while month_number != 0:
    if 1 <= month_number <= 12:
        print(f"El mes es: {myTupla[month_number - 1]}")
    else:
        print("Enter un numero valid")

    month_number = int(input("Enter un numero entre 1 and 12 (0 to exit): "))

print("Programa terminado.")
