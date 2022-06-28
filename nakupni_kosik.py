"""
nakupni_kosik.py: Úkol z Engeto akademie
author: Michal Kubín
email: kubin.michal@gmail.com
discord: Michal Kubín #0577
"""

import zadani
import funkce

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

    # Pokud je položka v košíku
    if polozka in kosik.keys():

        # Pokud je zboží skladem
        mnozstvi_polozky = zadani.potraviny[polozka][1]

        pocet = kosik[polozka] + 1
        kosik[polozka] = pocet
        print(kosik)

        funkce.sniz_stav_skladu(polozka)

        # Pokud zboží není skladem

    # Pokud není položka v košíku
    else:

        # Položka není v košíku, ale máme ji v nabídce
        if polozka in zadani.potraviny:
            kosik[polozka] = 1
            print(kosik)

            funkce.sniz_stav_skladu(polozka)


        # Položka vůbec není v nabídce
        else:

            # Pokud uživatel ukončil nákup pomocí "end"
            if polozka == "end":
                print("Nákup dokončen")
                print(kosik)

            # Pokud nákup neukončil, ale zadal špatnou položku
            else:
                print(f"Položka {polozka} není v nabídce.")



    # .. pokud hodnota na indexu 1 odpovídá 0 (není skladem)

# Finální výpis košíku po nákupu
