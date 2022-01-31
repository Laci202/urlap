print(
    """
    5.feladat:	Írd ki a 25 és -60 közötti számokat 
    pontosvesszővel elválasztva, úgy hogy az utolsó 
    után ne legyen pontosvessző. 
    """
)

#elvárt kimenet: 25, 24, 23, 22, 21, 20, ... -59,-60
#első megoldás az első elem megkülönböztetése
"""
szam=25
print(szam, end="")
for ciklusValtozo in range(24,-60-1,-1):
    print("; "+str(ciklusValtozo),end="")
"""
#második változat első megkülönböztetés while-al
szam=25
print(szam, end="")
ciklusValtozo=24
while ciklusValtozo > -61:
    print("; "+str(ciklusValtozo),end="")
    ciklusValtozo-=1