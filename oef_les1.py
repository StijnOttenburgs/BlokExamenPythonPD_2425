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