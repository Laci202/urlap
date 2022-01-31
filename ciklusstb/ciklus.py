def faktorialis(n):
    fakto = 1
    n = input("Irjon be egy számot: ")
    fakto = 1
    if int(n) >= 1:
        for i in range(1, int(n) + 1):
            faktorialis = fakto * i
        return fakto


num = int(input("Irjon be egy számot: "))

print("faktoriálisa: ", num, " (iterat.): ", end="")
print(faktorialis(num))