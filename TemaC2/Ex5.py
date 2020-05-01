print("""1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi
6 - Meniu""")

lista = []

while True:
    ok = input("\nIntroduceti comanda: ")
    if ok == "1":
        print("\tAfisare lista cumparaturi")
        print(lista)
    elif ok == "2":
        print("\tAdaugare element")
        adaug = input("Adauga: ")
        if not "." in adaug and not adaug.isdigit():
            lista.append(adaug)
        else:
            print("Elementul adaugat nu e aliment")
    elif ok == "3":
        print("\tStergere element")
        sterg = input("Sterge: ")
        if sterg in lista:
            lista.remove(sterg)
        else:
            print("Nu exista in lista.")
    elif ok == "4":
        print("\tStergere lista de cumparaturi")
        lista.clear()
        print("Lista a fost stearsa")
    elif ok == "5":
        print("\tCautare in lista de cumparaturi")
        caut = input("Cauta: ")
        if caut in lista:
            print("Produsul cautat exista:", caut)
        else:
            print("Produsul nu exista.")
    elif ok == "6":
        print("""\t1 – Afisare lista de cumparaturi
        2 – Adaugare element
        3 – Stergere element
        4 – Sterere lista de cumparaturi
        5 - Cautare in lista de cumparaturi
        6 - Meniu""")
    elif ok == "exit":
        exit()
    else:
        print("Alegerea nu exista. Reincercati.")