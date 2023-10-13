# feladat_014
# be: pozitív egész 
# ki: a szám páros vagy páratlan
# def használata 
#def my_function():
# utasítás

szam = 0

def beker_egy_szamot():
    szam = int(input("Kérek egy egész számot: "))
    return szam


def megoldas_if_else():
    if szam % 2 == 0:
        print(f"A számod {szam} páros!")
    else:
        print(f"A számod {szam} páratlan!")

    def megoldas_if_elif():
        if szam % 2 == 0:
            print(f"A számod {szam} páros!")
        elif szam % 2 == 1:
            print(f"A számod {szam} páratlan!")

 
def megoldas_if_elif_2():
        if szam % 2 == 0:
            print(f"A számod {szam} páros!")
        elif szam % 2 != 0:
            print(f"A számod {szam} páratlan!")


def megoldas_if_if():
        if szam % 2 == 0:
            print(f"A számod {szam} páros!")
        if szam % 2 == 1:
            print(f"A számod {szam} páratlan!")

#itt kezdődik a program
beker_egy_szamot()
megoldas_if_else()
megoldas_if_if()
