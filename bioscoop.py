# Programma vraagt hoeveel personen naar de film gaan.
# Per persoon wordt er naar naar de leeftijd.
# Daarna naar extra deze is voor iedereen hetzelfde


aant = int(input("Hoeveel personen gaan er naar de film?\n"))
leeftijd_personen = []
studentenkaarten = []
films_3d = []
inkomprijzen = []

for x in range(aant):
    leeftijd = int(input(f"Wat is de leeftijd van persoon {x+1}:\t"))
    leeftijd_personen.append(leeftijd)

    studentenkaart = False
    if leeftijd < 22:
        input_st = input("Heeft u een studentenkaart? (Ja/nee)").lower()
        if input_st == "ja":
            studentenkaart = True
    studentenkaarten.append(studentenkaart)

    drie_d = False
    input_3d = input("Gaat u naar een 3D film kijken? (ja/nee).").lower()
    if input_3d == "ja":
        drie_d = True
    films_3d.append(drie_d)

for i in range(aant):
    prijs_persoon = 0
    if films_3d[i] == True:
        prijs_persoon += 2
    if studentenkaarten[i] == True:
        if leeftijd_personen[i] <= 12:
            prijs_persoon += 5
        else:
            prijs_persoon += 6
    elif leeftijd_personen[i] <= 12:
        prijs_persoon += 5
    elif leeftijd_personen[i] <= 16:
        prijs_persoon += 6
    elif leeftijd_personen[i] <= 21:
        prijs_persoon += 7
    else:
        prijs_persoon += 9
    inkomprijzen.append(prijs_persoon)
    #print(prijs_persoon)

for j in range(aant):
    print(f"\nDe prijs voor persoon {j+1} is € {round(inkomprijzen[j],2)}.")
print(f"\nDe totaalprijs is € {round(sum(inkomprijzen),2)}.")
