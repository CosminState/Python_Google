
try:
    cnp = input("Adaugati CNP-ul: ")

    if not len(cnp) == 13:
        print("Lungimea CNP e gresita")
    elif not int(cnp[0:1]) in range(1, 9):
        print('CNP invalid')
    elif not int(cnp[3:5]) in range(1, 12):
        print('CNP invalid')
    elif not int(cnp[5:7]) in range(1, 31):
        print('CNP invalid')
    elif not int(cnp[7:9]) in range(1, 52):
        print('CNP invalid')
    elif not int(cnp[9:12]) in range(1, 999):
        print('CNP invalid')
    else:
        print('Se analizeaza CNP-ul: ', cnp)

        if int(cnp[0:1]) == 1 and int(cnp[1:3]) in range(00, 99):
            print('CNP acceptat\n' +
                  f'Sexul: masculin - Nascut in data {int(cnp[5:7])}.{int(cnp[3:5])}.19{int(cnp[1:3])}')
        elif int(cnp[0:1]) == 2 and int(cnp[1:3]) in range(00, 99):
            print('CNP acceptat\n' +
                  f'Sexul: feminin - Nascuta in data {int(cnp[5:7])}.{int(cnp[3:5])}.19{int(cnp[1:3])}')
        elif int(cnp[0:1]) == 3 and int(cnp[1:3]) in range(00, 99):
            print('CNP acceptat\n' +
                  f'Sexul: masculin - Nascut in data {int(cnp[5:7])}.{int(cnp[3:5])}.18{int(cnp[1:3])}')
        elif int(cnp[0:1]) == 4 and int(cnp[1:3]) in range(00, 99):
            print('CNP acceptat\n' +
                  f'Sexul: feminin - Nascuta in data {int(cnp[5:7])}.{int(cnp[3:5])}.18{int(cnp[1:3])}')
        elif int(cnp[0:1]) == 5 and int(cnp[1:3]) in range(00, 99):
            print('CNP acceptat\n' +
                  f'Sexul: masculin - Nascut in data {int(cnp[5:7])}.{int(cnp[3:5])}.20{int(cnp[1:3])}')
        elif int(cnp[0:1]) == 6 and int(cnp[1:3]) in range(00, 99):
            print('CNP acceptat\n' +
                  f'Sexul: feminin - Nascuta in data {int(cnp[5:7])}.{int(cnp[3:5])}.20{int(cnp[1:3])}')
        elif int(cnp[0:1]) == 7 and int(cnp[1:3]) in range(00, 99):
            print('CNP acceptat\n' +
                  f'Sexul: masculin - Persoana straina rezidenta in Romania ' +
                  f'- Nascut in data {int(cnp[5:7])}.{int(cnp[3:5])}.19{int(cnp[1:3])}')
        elif int(cnp[0:1]) == 8 and int(cnp[1:3]) in range(00, 99):
            print('CNP acceptat\n' +
                  f'Sexul: feminin - Persoana straina rezidenta in Romania ' +
                  f'- Nascuta in data {int(cnp[5:7])}.{int(cnp[3:5])}.19{int(cnp[1:3])}')
        elif int(cnp[0:1]) == 9 and int(cnp[1:3]) in range(00, 99):
            print('CNP acceptat\n' +
                  f'Sexul: masculin/feminin - Persoana straina ' +
                  f'- Nascut/a in data {int(cnp[5:7])}.{int(cnp[3:5])}.19{int(cnp[1:3])}')
        else:
            print('CNP incorect')

except Exception as e:
    print("Adaugati un CNP valid")