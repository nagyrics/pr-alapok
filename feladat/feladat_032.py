# feladat_032

#Listák rendezése
#Rendezés

nyelvek = ['Python', 'C', 'C++', 'Java']

# sorbarendezi a listát
nyelvek.sort()

# fordított sorrendbe rendezi a listát
nyelvek.reverse()  
 
#A listák a sort() és reverse() metódusok hatására módosulnak, elemeik rendezett sorban helyezkednek el.
# ----------------------------------------------------------------------

#Keresés a listákban

    # az adott elem első előfordulásának indexe
print(nyelvek.index('C'))

    # az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

    # NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)

# ----------------------------------------------------------------------

#Listák bővítése

    # a lista végére hozzáfűz egy elemet
nyelvek.append('Python')
   
    # a listát másolja
nyelvek_masolat = nyelvek.copy()
   
    # a lista végére hozzáfűz egy másik gyűjteményt (pl. listát)
nyelvek_honlapkesziteshez = ['HTML', 'CSS', 'JavaScript']
nyelvek.extend(nyelvek_honlapkesziteshez)
   
    # adott indexű helyre beszúrja a megadott elemet
nyelvek.insert(1, 'Go')  

# ----------------------------------------------------------------------
#Törlés a listákban

    # eltávolítja a legutolsó elemet, és azzal tér vissza
    # itt például a törölt értéket a 'torolt_nyelv' fogja tartalmazni
nyelvek.pop()
torolt_nyelv = nyelvek.pop()

    # eltávolítja a megadott indexű elemet,  és azzal tér vissza
nyelvek.pop(1)

    # eltávolítja a megadott indexű elemet
del nyelvek[1]

    # eltávolítja a megadott elemet az elsőként megtalált pozícióból
nyelvek.remove('Python')
    # törli a listát
nyelvek.clear()
