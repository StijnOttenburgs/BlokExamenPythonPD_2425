# realtime currency converter
import requests

def oproep_wisselkoers(originele_valuta,nieuwe_valuta):
    url = f"https://api.frankfurter.app/latest?from={originele_valuta.upper()}&to={nieuwe_valuta.upper()}"
    antwoord = requests.get(url)
    data = antwoord.json()
    return data['rates'][nieuwe_valuta.upper()]

def currency_converter(originele_valuta,nieuwe_valuta,bedrag):

    wisselkoers = oproep_wisselkoers(originele_valuta.lower(),nieuwe_valuta.lower())
    print(f"De huidige wisselkoers ({originele_valuta} --> {nieuwe_valuta}): {wisselkoers:.2f}")

    bedrag_nieuwe_valuta = wisselkoers * bedrag
    print(f"{bedrag} {originele_valuta.upper()} = {bedrag_nieuwe_valuta} {nieuwe_valuta.upper()}")

currency_converter("eur","gbp",100)

# gemiddelde van 3 getallen
def gemiddelde(lijst):
    for i in lijst:
        if type(i) == "int" or "float":
            continue
        else:
            print("Geef enkel cijfers in de lijst waarvan u het gemiddelde wenst te berekenen.")
    lengte = len(lijst)
    totaal = sum(lijst)
    print(f"Het gemiddelde van de onderstaande lijst is {sum(lijst)/len(lijst):.2f}\n",lijst)

import random
getallen = []
for _ in range(100):
    getallen.append(random.uniform(0,10000))

gemiddelde(getallen)

# omrekencalculator temperatuur
def calculator_temp():
    orig_eenheid = int(input("Kies uit één van de volgende opties voor de temperatuureenheid die u wil omrekenen:\n"
                         "1: Fahrenheit\n"
                         "2: Kelvin\n"
                         "3: Celsius\n"))
    nieuwe_eenheid = int(input("Kies uit één van de volgende opties voor de temperatuureenheid waarnaar u wil omrekenen:\n"
                         "1: Fahrenheit\n"
                         "2: Kelvin\n"
                         "3: Celsius\n"))
    if orig_eenheid == 1:
        temp_orig_eenheid = float(input("Geef de temperatuur die u wil omrekenen in Fahrenheit.\n"))
        if nieuwe_eenheid == 1:
            print("De starteenheid en eindeenheid zijn hetzelfde")
        elif nieuwe_eenheid == 2:
            temp_nieuwe_eenheid = (temp_orig_eenheid - 32) * 5/9 + 273.15
            print(f"{temp_orig_eenheid:.2f} °F = {temp_nieuwe_eenheid:.2f} K")
        elif nieuwe_eenheid == 3:
            temp_nieuwe_eenheid = (temp_orig_eenheid - 32) * 5/9
            print(f"{temp_orig_eenheid:.2f} °F = {temp_nieuwe_eenheid:.2f} °C")
        else:
            print("Foute invoer!")

    elif orig_eenheid == 2:
        temp_orig_eenheid = float(input("Geef de temperatuur die u wil omrekenen in Kelvin.\n"))
        if nieuwe_eenheid == 1:
            temp_nieuwe_eenheid = (temp_orig_eenheid - 273.15) * 9/5 + 32
            print(f"{temp_orig_eenheid:.2f} K = {temp_nieuwe_eenheid:.2f} °F")
        elif nieuwe_eenheid == 2:
            print("De starteenheid en eindeenheid zijn hetzelfde")
        elif nieuwe_eenheid == 3:
            temp_nieuwe_eenheid = (temp_orig_eenheid - 273.15)
            print(f"{temp_orig_eenheid:.2f} K = {temp_nieuwe_eenheid:.2f} °C")
        else:
            print("Foute invoer!")

    elif orig_eenheid == 3:
        temp_orig_eenheid = float(input("Geef de temperatuur die u wil omrekenen in Celsius.\n"))
        if nieuwe_eenheid == 1:
            temp_nieuwe_eenheid = temp_orig_eenheid * 9/5 + 32
            print(f"{temp_orig_eenheid:.2f} °C = {temp_nieuwe_eenheid:.2f} °F")
        elif nieuwe_eenheid == 2:
            temp_nieuwe_eenheid = (temp_orig_eenheid + 273.15)
            print(f"{temp_orig_eenheid:.2f} °C = {temp_nieuwe_eenheid:.2f} K")
        elif nieuwe_eenheid == 3:
            print("De starteenheid en eindeenheid zijn hetzelfde")
        else:
            print("Foute invoer!")

    else:
        print("Foute invoer!")



calculator_temp()

#Schrijf een programma dat de kostprijs weergeeft om een balk 70 % met water te vullen. De prijs bedraagt 0,38 cent per m³.
lengte = float(input("Wat is de lengte van de balk in m?\n"))
breedte = float(input("Wat is de breedte van de balk in m?\n"))
hoogte = float(input("Wat is de hoogte van de balk in m?\n"))
prijs_water = 0.0038 # €/m³
volume = lengte * breedte * hoogte
print(f"Het volume van de balk is {volume:.2f} m³.\n"
      f"70% van dit volume is {0.7*volume:.2f} m³.\n"
      f"De waterprijs bedraagt {prijs_water} €/m³.\n"
      f"De prijs om deze balk 70% met water te vullen bedraagt € {0.7*volume*prijs_water:.2f}.")

# Schrijf een programma dat de schuine zijde van een rechthoekige driehoek geeft. a = sqrt(b² + c²)
from math import sqrt
b = float(input("Geef de eerste rechthoekszijde in?"))
c = float(input("Geef de tweede rechthoekszijde in?"))
a = sqrt(b ** 2 + c ** 2)
print(a)

import math

def oppervlakte_vijfhoek(zijde):
    # Formule voor de oppervlakte van een regelmatige vijfhoek
    oppervlakte = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * zijde**2
    return oppervlakte

# Vraag de gebruiker om de lengte van een zijde
zijde = float(input("Geef de lengte van een zijde van de vijfhoek: "))

# Bereken en toon de oppervlakte
oppervlakte = oppervlakte_vijfhoek(zijde)
print(f"De oppervlakte van de vijfhoek is: {oppervlakte:.2f}")
