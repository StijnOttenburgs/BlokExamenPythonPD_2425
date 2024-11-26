# Een bedrijf dat teambuildings aanbiedt heeft een calculator nodig.
# Zie activiteiten in de tabel(volgende slide).
# Maak een list met de namen van de activiteiten
# Per activiteit wordt er gevraagd naar het aantal deelnemers.
# Ook wordt er gevraagd hoeveel deelnemers een optie willen, indien dit er is.
# Maak voor elke activiteit een functie die een waarde returnt naar een list. Indien geen inschrijven returnt het programma 0 in de list
# Geef uiteindelijk de totaal kost, en kost per activiteit. Hoeveel kost de duurste activititeit(enkel bedrag, niet de naam van de activititeit)

def teambuilding():
    activiteiten = {"Schaatsen":
                        {"prijs optie":5,
                         "prijs activiteit":15},
                    "Karten":
                        {"prijs optie":15,
                         "prijs activiteit":20},
                    "Boswandeling":
                        {"prijs optie":0,
                         "prijs activiteit":5}
                    }
    lijst_opbrengsten = []

    for k,v in activiteiten.items():
        print(f"Activiteit: {k}")
        aant_deelnemers = int(input("Wat is het aantal deelnemers?\n"))
        deelnemers_opties = int(input("Wat is het aantal deelnemers dat de extra optie wil?\n"))
        if aant_deelnemers == 0:
            lijst_opbrengsten.append(0)
        else:
            prijs = aant_deelnemers * v["prijs activiteit"] + deelnemers_opties * v["prijs optie"]
            lijst_opbrengsten.append(prijs)

    print(f"De totaal opbrengsten zijn € {round(sum(lijst_opbrengsten))}.")
    for i in range(len(lijst_opbrengsten)):
        print(f"De opbrengst voor activiteit {i+1} is € {round(lijst_opbrengsten[i])}.")
    print(f"De duurste activiteit kost € {round(max(lijst_opbrengsten))}.")

teambuilding()