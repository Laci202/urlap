def haromszogg(a, b, c):
    if (a + b > c and a + c > b and b + c > a):
        print("Háromszög formázás lehetséges", a, b, c, "oldalaknak")
    else:
        print("Háromszög nem lehet formázva az adott számokkal", a, b, c, "oldalaknak")


a = int(input("Irjon be egy számot:"))
b = int(input("Irjon be egy számot:"))
c = int(input("Irjon be egy számot:"))

haromszogg(a, b, c)