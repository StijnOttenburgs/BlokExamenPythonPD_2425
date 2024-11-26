def boekhoudprogramma():
    status = "x"
    bedrag_excl_btw = 0
    ex_btw = []
    in_btw = []
    while status.lower() != "einde":
        status = input("Indien u het programma wenst te beëindigen geef 'einde' in, indien u wenst door te gaan hoeft u enkel op enter te duwen:\n")
        if status.lower() != "einde":
            bedrag_excl_btw = float(input("Geef een bedrag exclusief BTW in:\n"))
            btw_percentage = float(input("Geef het gewenste btw percentage in (0.06 of 0.21):\n"))
            ex_btw.append(bedrag_excl_btw)
            in_btw.append(bedrag_excl_btw*(1+btw_percentage))

    print(f"Het totaal exclusief btw is € {sum(ex_btw)}.\n"
          f"Het totaal inclusief btw is € {sum(in_btw)}.\n"
          f"De lijsten kunnen geraadpleegd worden. (ex_btw & in_btw).")


boekhoudprogramma()
print (in_btw)
