# feladat_027
# Lista bejárása index-szel I.

honapok = ['január', 'február','március', 'április', 'május', 'június']

index = 0 
for honap in honapok:
    # az eredeti listaelem NEM módosul!
    print(index, honap)
    index = index + 1
    
for index in range(len(honapok)):
    # az eredeti listaelem módosul!
    honapok[index] = honapok[index].upper()
    print(honapok)
        
for index in range(len(honapok)):
    honapok[0,2,4] = honapok [index].lower
    print(honapok)