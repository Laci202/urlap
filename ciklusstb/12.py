kezdes = int(input("Irjon be egy számot "))
veg = int(input("Irjon be egy számot "))

# iterating each number in list
for num in range(kezdes, veg + 1):

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")