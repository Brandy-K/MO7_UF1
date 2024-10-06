myDict = {"Euro": "€", "Dollar": "$", "Pound": "£", "Yen": "¥"}

currency = input("Enter una divisa: ")

if currency in myDict:
    print(f"El simbol de la divisa {currency} es {myDict[currency]}:")
else:
    print(f"El simbol de la divisa {currency} no esta")
