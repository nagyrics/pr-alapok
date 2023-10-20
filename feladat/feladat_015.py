#feladat_015
"""
Kérjük be a vezeték és keresztnevüket 
Írassuk ki függvény segíségével nevünket.
pl:
Be:"Kérem a vezetékneved : Takács"
Be:"Kérem a keresztneved : István"
Ki: "A nevem: Takács István"
"""

vezeteknev= input("Kérek egy vezetéknevet! ")
keresztnév= input("Kérek egy keresztnevet! ")
def nevf(vnev,knev):
    nevem = vnev + ' ' + knev
    return nevem

print(f"A nevem: {nevf(vezeteknev,keresztnév)}")