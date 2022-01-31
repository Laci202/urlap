print(
    """
    Minta alapján írjuk i a 12-es szorzótáblát!
    """
)
#első sor
print("      ")
for szam in range(1,13,1):
    print(" {:4d}".format(szam), end="")
print("")
#második sor
print("  :", end="")
for sorszam in range(0,57,1):
    print("-", end="")


