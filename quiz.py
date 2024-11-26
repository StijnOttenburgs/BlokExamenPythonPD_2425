# Maak een quiz met 5 vragen over de hoofdsteden.
# Indien de gebruiker goed antwoord,krijgt hij een punt.
# Geef na elke vraag feedback, Prima, of Fout het juiste antwoord was.

def quiz():
    punten = 0
    vragen = {
        "Moskou":"Wat is de hoofdstad van Rusland?",
        "Brussel": "Wat is de hoofdstad van België?",
        "Rome": "Wat is de hoofdstad van Italië?",
        "Parijs": "Wat is de hoofdstad van Frankrijk?",
        "Berlijn": "Wat is de hoofdstad van Duitsland?",
    }
    for k,v in vragen.items():
        print(v)
        invoer = input()
        if invoer.capitalize() == k:
            print("Prima, goed antwoord!")
            punten +=1
        else:
            print(f"Fout, het juiste antwoord is  {k}.")

    if punten == 0:
        print("0/5 : Je bent wereldvreemd")
    elif punten == 1:
        print("1/5 : Je had beter moeten opletten in de les")
    elif punten == 2:
        print("2/5: Best de hoofdsteden nog eens herhalen")
    elif punten == 3:
        print("3/5: Geslaagd maar herhalen kan geen kwaad.")
    elif punten == 4:
        print("4/5: Bijna alles juist, je bent goed bezig")
    else:
        print("5/5: Proficiat je bent een wereldburger")

quiz()

