#feladat_021
#Egymásba ágyazott ciklusok II.

szam = int(input(f'Kérek egy páros számot: '))
szamfele = int(szam/2)

darab_karakter = 1
sor = 1
while sor <= szamfele:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1

darab_karakter = szamfele
sor = 1
while sor <= szamfele:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1