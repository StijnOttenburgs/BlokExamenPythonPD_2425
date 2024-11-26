# Mastermind tussen stap
# Raad 4 kleuren, rood, blauw, geel, groen

"""import random as rd
def mastermind_kleur():
    kleuren = ["rood","blauw","geel","groen"]
    generator = []
    for i in range(4):
        generator.append(rd.choices(kleuren))

    keuze = []
    for i in range(4):
        keuze.append(input("Kies 1 kleur uit de volgende opties:\n"
                           "* rood\n"
                           "* blauw\n"
                           "* geel\n"
                           "* groen\n"
                           "Maak je keuze:\t"))

    juist = 0
    for i in range(4):
        if keuze[i] == generator[i]:
            juist += 1

    print(f"Je hebt {juist} kleuren juist geraden!")

mastermind_kleur()"""

import random as rd
def mastermind():
    kleuren = ["R", "G", "B"]
    cijfers = ["1","2","3","4"]

    generator = [rd.choice(kleuren)+rd.choice(cijfers) for _ in range(4)]

    print("Raad een reeks van 4 combinaties van kleur en nummer (bijv. 'R1', 'G3', 'B2', 'B2').")
    print("Kleuren: R (rood), G (geel), B (blauw). Nummers: 1-4.")
    print("Geef je invoer in het formaat: R3 G3 B2 G3")

    while True:
        invoer = input("Voer je reeks in:\n").upper().split() # Maakt een list van de ingevoerde str

        #invoer controleren
        if len(invoer) != 4 or any(len(combo) != 2 for combo in invoer):
            print("Ongeldige invoer! Zorg ervoor dat je vier combinaties invoert zoals 'R1'. Probeer opnieuw.")
            continue

        feedback = []

        for i in range(4):
            kleur, cijfer = invoer[i][0], invoer[i][1]
            correct_kleur, correct_cijfer = generator[i][0], generator[i][1]

            if invoer[i] == generator[i]:
                feedback.append("Beide correct!")
            elif kleur == correct_kleur:
                feedback.append("Correcte kleur!")
            elif cijfer == correct_cijfer:
                feedback.append("Correct cijfer!")
            else:
                feedback.append("Fout!")

        print("Feedback op je invoer:",' | '.join(feedback))

        if invoer == generator:
            print("Gefeliciteerd! Je hebt de reeks juist geraden.")
            break
        else:
            print("Niet helemaal juist, probeer het opnieuw.\n")




mastermind()



