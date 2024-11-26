# Een schilder vraagt 35 euro per uur ex btw,
# Hij schildert 18m² op 1 uur, dit is 1 laag.
# Het programma vraagt het aantal muren.
# De verf kost 15 euro per l ex btw. 1 liter is 22m²
#prijs voor 3 lagen incl btw

def schilder():
    tarief_u = 35 # €/u
    tempo_u = 18 # in m²
    prijs_verf = 15 # in euro per l, excl btw
    rendement_verf = 22 # in m²/l
    aant_muren = int(input("Hoeveel muren heeft u om te laten verven?\n"))
    opp_muren = [] # in m²
    counter = 0 # om weer te geven om welke muur het in de reeks gaat
    for _ in range(aant_muren):
        counter += 1
        print(f"Muur {counter}:")
        l_muur = float(input(f"Wat is de lengte van muur {counter} in m?\n"))
        h_muur = float(input(f"Wat is de hoogte van muur {counter} in m?\n"))
        opp_muren.append(l_muur*h_muur)
        print(f"De oppervlakte van deze muur is {opp_muren[-1]} m².")

    prijs = ((sum(opp_muren)/rendement_verf) * prijs_verf + (sum(opp_muren)/tempo_u) * tarief_u) * 3 * 1.21
    print(f"De totale oppervalkte van al uw muren is {round(sum(opp_muren),2)} m².\n"
          f"De kostprijs om al uw muren te laten verven voor 3 lagen verf bedraagt € {round(prijs,2)}.")

schilder()


