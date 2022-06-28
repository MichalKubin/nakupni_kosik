"""
nakupni_kosik.py: Úkol z Engeto akademie
author: Michal Kubín
email: kubin.michal@gmail.com
discord: Michal Kubín #0577
"""

import zadani

# Úvodní sekce s uvítáním a výpisem zboží

print("Vitejte našem nákupním košíku!")
print(zadani.oddelovac)
print(zadani.nabidka)

# Cyklus, který přidává zboží do košíku tak dlouho, jak uživatel zamýšlí
polozka = ""
kosik = zadani.kosik

while polozka != "end":
    polozka = input("Zadejte název zboží (dle ceníku), které chcete vložit "
                    "do košíku: ")
    if polozka in kosik.keys():
        pocet = kosik[polozka] + 1

        kosik[polozka] = pocet
        print(kosik)

    else:

        if polozka in zadani.potraviny:
            kosik[polozka] = 1
            print(kosik)
        else:
            print(f"Položka {polozka} není v nabídce.")
    """
    print(polozka)
    if kosik[polozka]:
        kosik[polozka] = 1
    else:
        kosik[polozka] = kosik[polozka] + 1
    """

    # .. pokud uživatel nezadá zboží z nabídky

    # .. pokud zboží ještě v košíku není

    # .. pokud se již vybrané zboží nachází v košíku

    # .. pokud hodnota na indexu 1 odpovídá 0 (není skladem)

# Finální výpis košíku po nákupu
