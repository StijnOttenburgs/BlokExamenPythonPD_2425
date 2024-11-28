vb_lijst = ["Jonas","Stijn","Joris","Ben"]

def voeg_naam_toe(naam):
    # create: nieuw record aanmaken in lijst
    vb_lijst.append(naam.capitalize())
    print(f"{naam.capitalize()} is toegevoegd.")

def toon_namen():
    print("De namen in de lijst zijn:")
    for naam in vb_lijst:
        print(naam)

def wijzig_naam(oorspronkelijk_naam, nieuwe_naam):
    # read en update van een record
    if oorspronkelijk_naam.capitalize() in vb_lijst:
        vb_lijst[vb_lijst.index(oorspronkelijk_naam.capitalize())] = nieuwe_naam.capitalize()
        print(f"{oorspronkelijk_naam.capitalize()} is vervangen door {nieuwe_naam.capitalize()}.")
    else:
        print(f"{oorspronkelijk_naam.capitalize()} is niet teruggevonden in de lijst.")

def verwijder_naam(naam):
    if naam.capitalize() in vb_lijst:
        vb_lijst.remove(naam.capitalize())
        print(f"{naam.capitalize()} is verwijderd.")
    else:
        print(f"{naam.capitalize()} is niet teruggevonden in de lijst.")

def crud():
    invoer = ""
    while invoer.lower() != "stop":
        print("1: toon lijst")
        print("2: voeg toe aan lijst")
        print("3: verwijder uit lijst")
        print("4: pas naam x aan uit lijst")
        print("STOP: stop de CRUD-functie")
        invoer = input(("Geef je keuze:\n"))
        if invoer.strip() == "1":
            toon_namen()
        elif invoer.strip() == "2":
            voeg_naam_toe(input("Geef de naam die je wil toevoegen:\n"))
        elif invoer.strip() == "3":
            verwijder_naam(input("Geef de naam die je wil verwijderen:\n"))
        elif invoer.strip() == "4":
            wijzig_naam(input("Geef de naam die je wil aanpassen:\n"),
                                input("Geef de nieuwe naam waarmee je de oorspronkelijke naam wil vervangen:\n"))
        elif invoer.strip().lower() == "stop":
            print("CRUD-functie gestopt.")
            break
        else:
            print("Foutieve invoer!")


import platform
print(dir(platform))