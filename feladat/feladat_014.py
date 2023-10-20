#feladat_014
"""
Kérjük be a vezeték és keresztnevüket 
Írassuk ki eljárás segíségével nevünket.
pl:
Be:"Kérem a vezetékneved : Takács"
Be:"Kérem a keresztneved : István"
Ki: "A nevem: Takács István"
"""

vezeteknev= input("Kérek egy vezetéknevet! ")
keresztnév= input("Kérek egy keresztnevet! ")
def nev(vnev,knev):
    print(f"A nevem: {vnev} {knev}")

nev(vezeteknev,keresztnév)