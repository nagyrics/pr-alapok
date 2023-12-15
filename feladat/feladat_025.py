# feladat_025

tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']
szamlalo = 0
index = 0

for tantargy in tantargyak:
    print( f"A tantárgyak lista {index}. indexű eleme: {tantargy}" )
    szamlalo += 1
    index += 1
print( f"A {szamlalo} eleme van a tantárgyak listának." )
