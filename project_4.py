ukoly = [] # Seznam pro uchovávání úkolů

# Funkce pro hlavní menu
def hlavni_menu():
    while True:
        print("Hlavní menu:")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = int(input("Vyber možnost (1-4): "))

        if volba == 1: #pri zadani cisla 1 se prida úkol 
            pridat_ukol()
        elif volba == 2: #pri zadani cisla 2 se zobrazí úkoly
            zobrazit_ukoly()
        elif volba == 3: #pri zadani cisla 3 se bude odstranovat úkol 
            odstranit_ukol()
        elif volba == 4: #pri zadani cisla 4 ukončíme program
            print("Program končí")
            break
        else:
            print("Neplatná volba, zadejte číslo mezi 1 a 4.")

# Funkce pro přidání úkol
def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ")
        if nazev == "": #pokud uživatel nezadá název úkolu program vypíše chybovou hlášku a poté bude muset zadat znova název úkolu
            print("Název úkolu nesmí být prázdný.")
            continue
        popis = input("Zadejte popis úkolu: ")
        if popis == "": #pokud uživatel nezadá popis úkolu program vypíše chybovou hlášku a poté bude muset zadat znova popis úkolu
            print("Popis úkolu nesmí být prázdný.")
            continue
        ukol = {'nazev': nazev,
                'popis': popis
                }
        ukoly.append(ukol)
        print("Úkol 'nazev' byl úspěšně přidán")
        break
        
# Funkce pro zobrazení úkolů
def zobrazit_ukoly():
    if not ukoly: #pokud nejsou úkoly k zobrazení vypíše hlášku "Žádné úkoly nejsou k dispozici."
        print("Žádné úkoly nejsou k dispozici.")
    else: #vypíše seznam úkolů
        print("Seznam úkolů")
        for i, ukol in enumerate(ukoly):
            print(f"{i}: {ukol['nazev']}")

# Funkce pro odstranění úkolu
def odstranit_ukol():
    if not ukoly: #pokud nemáme žádné úkoly vypíše hlášku "Žádné úkoly nejsou k dispozici k odstranění"
        print("Žádné úkoly nejsou k dispozici k odstranění.")
    else: #zobrazí úkoly k odstranění
        while True:
            zobrazit_ukoly()
            cislo_ukolu = int(input("Zadejte číslo úkolu, který chcete odstranit."))
            if cislo_ukolu == "": #pokud uzivatel nezada žádné číslo úkolu vypíše to hlášku že pole nesmí byt prázdné
                print("Číslo úkolu nesmí být prázdné.")
                continue
            if cislo_ukolu <0 or cislo_ukolu > len(ukoly)-1: #pokud uzivatel zadá číslo úkolu který neexistuje požádá ho to o nové číslo
                print("Číslo úkolu neexistuje.") 
                continue
            else:
                ukoly.pop(cislo_ukolu) 
            print("Úkol byl odstraněn")
            break
   

# Spuštění programu
hlavni_menu()