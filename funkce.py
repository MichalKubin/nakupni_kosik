import zadani

def sniz_stav_skladu(value):
    mnozstvi_polozky = zadani.potraviny[value][1]
    novy_pocet = mnozstvi_polozky - 1
    zadani.potraviny[value][1] = novy_pocet
    print(f"Nový stav skladu položky {value}:"
          f" {zadani.potraviny[value][1]}")