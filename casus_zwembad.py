def kost_zwembad():
    import math

    vorm = input("Wat is de gewenste vorm van het zwembad?\n"
                 "Kies uit de volgende opties: kubus, rechthoek of cilinder.\n")
    hoogte = float(input("Wat is de diepte van het zwembad (in meter)?"))
    if vorm.lower() == "kubus":
        z = float(input("Geef de zijde (lengte & breedte) van het zwembad in (in meter)?\n"))
        volume = z**2 * hoogte
    elif vorm.lower() == "rechthoek":
        l = float(input("Geef de lengte van het zwembad in (in meter)?\n"))
        b = float(input("Geef de breedte van het zwembad in (in meter)?\n"))
        volume = l* b * hoogte
    elif vorm.lower() == "cilinder":
        dia = float(input("Geef de diameter van het zwembad in (in meter)?\n"))
        volume = (dia/2)**2 * math.pi * hoogte
    else:
        print("U heeft een foutieve vorm ingegeven probeer opnieuw!")

    materiaal = input("In welk materiaal wenst u het zwembad (kunststof of metaal)?\n")

    if materiaal.lower() == "kunststof":
        prijs = volume * (250+0.85)
    elif materiaal.lower() == "metaal":
        prijs = volume * (320 + 0.85)
    else:
        print("U heeft een foutief materiaal ingegeven probeer opnieuw!")

    print(f"U heeft een zwembad gekozen uit {materiaal} in de vorm van een {vorm}.\n"
          f"Het volume van het zwembad is {round(volume)} m³.\n"
          f"De kostprijs is € {round(prijs)}.")

kost_zwembad()