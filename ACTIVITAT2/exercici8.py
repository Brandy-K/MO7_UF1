words = input("Enter 1 to 3 words: ").split()
if len(words) == 0 or len(words) > 3:
   print("enter paraules entre 1 i 3")
else:
   for i in words:
       print(f"Word: {i}, Length: {len(i)}, First character: {i[0]}, Last character: {i[-1]}")
