value = float(input("valor en €: "))
while True:
    vat = float(input("VAT (4, 10, or 21): "))
    if vat==4 or vat==10 or vat==21:
     print(value+value*vat/100)
else:
    print("enter a valid VAT.")
