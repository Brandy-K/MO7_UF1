paraula1 = input("Enter la primera paraula: ")
paraula2 = input("Enter la segona paraula: ")

if len(paraula1) >= 2 and len(paraula2) >= 2:
    new_word1 = paraula2[:2] + paraula1[2:]
    new_word2 = paraula1[:2] + paraula2[2:]
    print(f"New words: {new_word1}, {new_word2}")
else:
    print("paraules son curts.")
