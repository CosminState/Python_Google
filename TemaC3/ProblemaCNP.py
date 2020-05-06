
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
        print('CNP acceptat:', cnp)
except Exception as e:
    print("Adaugati un CNP valid")