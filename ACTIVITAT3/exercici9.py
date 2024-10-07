assignatures = ["Math", "Science", "History", "English", "Art", "Physical Education"]
notes = []   # to store the new notes

for subject in assignatures:
    nota = float(input(f"Enter la nota de {subject}: "))
    notes.append(nota)

for i in range(len(assignatures)):
    print(f"{assignatures[i]} ha tret {notes[i]}")
