frase = input("Enter una frase: ")

fraseSenseEspai = tuple(frase.replace(" ", ""))
frase_tupla = tuple(fraseSenseEspai)
print("Frase tupla es: ",frase_tupla)
fraseSenseRepetirs = "".join(dict.fromkeys(fraseSenseEspai))
print("Frase sense caracters repetits: ",  {fraseSenseRepetirs})
