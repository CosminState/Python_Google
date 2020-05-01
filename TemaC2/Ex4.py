nr = float(input("Introdu un numar: "))

if nr > 0:
    if nr < 10:
        print("Numarul este mai mare ca 0, dar mai mic ca 10.")
    else:
        print("Numarul este mai mare ca 10.")
elif nr == 0:
    print("Numarul este 0 .")
else:
    print("Numarul este:", abs(nr))