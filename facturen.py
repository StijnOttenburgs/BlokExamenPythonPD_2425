def facturen():
    status = ""
    aankopen = []
    verkopen = []
    counter = 1
    while status != "stop":
        print(f"Product {counter}")
        counter += 1
        aankoop = float(input("Wat is de aankoopprijs van de factuur:\n"))
        verkoop = float(input("Wat is de verkoopprijs van de factuur:\n"))
        aankopen.append(aankoop)
        verkopen.append(verkoop)
        status = input("Geef stop in als u wenst te stoppen, druk op enter indien u wenst door te gaan:\n")

    resultaat = sum(verkopen) - sum(aankopen)
    if resultaat > 0:
        print(f"De winst van de ingegeven facturen is € {round(resultaat)}.\n"
              f"Dit geeft een winst van {round(resultaat/sum(aankopen)*100)}%.")
    elif resultaat ==0:
        print(f"Er is geen winst of verlies gemaakt.")
    else:
        print(f"Het verlies van de ingegeven facturen is € {round(resultaat)*(-1)}.\n"
              f"Dit geeft een verlies van {round(resultaat / sum(aankopen) * 100)}%.")

facturen()
