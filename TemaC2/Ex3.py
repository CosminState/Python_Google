an = input("Introdu un an: ")

if an.isdigit():
    if int(an) % 4 == 0:
        print("Anul este bisect")
    else:
        print("Anul nu este bisect")
else:
    print("Introdu un an valid")