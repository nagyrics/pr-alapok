# feladat_016
# While ciklus III.

folytatja = True
while folytatja:
    print('Vidd ki a szemetet! ')
    valasz = input('Mondjam mégegyszer? (I/N): ')
    if valasz == 'N':
        folytatja = False 

print(f"A program vége.")
