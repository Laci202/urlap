
 # rekurzió használata
def faktorial(N): #rand..+n.
    arr = {} #arrange
    if N in arr:
        return arr[N]
    elif N == 0 or N == 1:
        return 1
        arr[N] = 1
    else:
        fakt = N * faktorial(N - 1)
        arr[N] = fakt
    return fakt


num = int(input("Irjon be egy számot "))

print("faktoriálisa: ", num, " (dynamic): ", end="")
print(faktorial(num))