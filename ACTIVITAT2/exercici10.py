import random
num_cert = random.randint(1, 100)
intent = 0
while True:
    prova = int(input("enter numero entre 1 i 100: "))
    intent += 1

    if prova < num_cert:
        print("numero es petit")
        if prova > num_cert:
            print("numero es mes gran")
    else:
        print(f"El numero: {prova} es correcte i numero d'intents son {intent}")
