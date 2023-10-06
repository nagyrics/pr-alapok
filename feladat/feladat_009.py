# feladat_009
"""
Kérjünk be két egész számot, szám1 és szám2
hasonlitsuk össze a két számot, és irassuk ki, hogy
a szám1 kisebb mint a szám2,
vagy a szám2 kisebb mint a szám1, 
vagy a szám1 egyenlő szám2-vel.


"""

szám1 = input("Írj be egy egész számot:")
szám2 = input("Írj be még egy egész számot:")
szám1 = int(szám1)
szám2 = int(szám2)




if szám1 > szám2:
    print(f" szám1 nagyobb mint szám2")
elif szám1 < szám2:
    print(f"{szám1} kisebb mint {szám2}")
elif szám1 == szám2:
    print(f"{szám1} egyenlő {szám2}-vel")



    

    