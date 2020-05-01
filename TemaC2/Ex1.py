nume = input("Introdu numele tau: ")

caract = "caractere"
numere = "numere"

if not "." in nume and not "," in nume and not nume.isdigit():
    intr = input("Inotrdu un sir de caractere sau un sir de numere: \n")

    if len(intr) > 0:
        floatSign = 1
        if intr[0] == "-":
            floatSign = -1
            intr = intr[1:]
        a = None
        if intr.isdigit():
            print(f"Sirul de {numere} a fost gasit de {nume.capitalize()}")
        elif "." in intr and len(a := intr.split(".")) == 2 and a[0].isdigit() and a[1].isdigit():
            intr = float(intr)
            print(f"Sirul de {numere} a fost gasit de {nume.capitalize()}")
        elif isinstance(intr, str):
            print(f"Sirul de {caract} a fost gasit de {nume.capitalize()}")
else:
    print("Te rog sa bagi un nume valid.")
