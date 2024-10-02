num = int(input("Enter number between 10 and 100: "))

if num >= 10 or num <= 100:
    num = tuple(range(1, num+1))
    print(num)
else:
    print("Enter number between 10 and 100")
