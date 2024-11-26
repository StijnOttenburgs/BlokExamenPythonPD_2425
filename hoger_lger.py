# Het programma kiest een willekeurig getal tussen 1 en 100
# Als gebruiker doe je een gok.
# Indien jouw getal groter is zegt het programma kleiner en visa versa
# Indien het juist is. Zegt jouw programma goedzo en geeft het aantal beurten.

def hoger_lager():
    import random as rd
    getal = rd.randint(1,100)
    gok = 0
    counter = 0
    while gok != getal:
        counter += 1
        gok = int(input("Kies een geheel getal tussen 1 en 100:\n"))
        if gok == getal:
            print(f"Goed zo, je hebt het getal geraden in {counter} beurten!")
        elif gok > getal:
            print("Lager!")
        else:
            print("Hoger!")

hoger_lager()