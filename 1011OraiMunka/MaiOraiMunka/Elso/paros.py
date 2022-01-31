#modul
import random

def parosEgesz():
    szam = random.randint(-1000, 1000)
    # db=1
    while not(szam%2==0):
        szam = random.randint(-1000, 1000)
    return szam