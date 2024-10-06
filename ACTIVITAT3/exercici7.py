myDict = {}
afegir = True
while afegir:
    user_name = input("Enter the name: (Enter stop to stop the program)")
    if user_name == 'stop':
        afegir = False
    else:
        user_age = input("Enter the age: ")
        if user_name in myDict:
            print("This username exists!!")
        else:
            myDict[user_name] = user_age
            print(myDict)

