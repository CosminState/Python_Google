#print('\tPrimul meu string pentru \ncurs 2')  #\t pune un tab
#print('Primul meu string pentru curs 2. ' * 2)

#print(2+2*2-2/1)  #ridicare putere: **

#a = "String"
#a += "String1"
#print(type(a))

#concatenare cu format
#a = "String1"
#b = "String2"
#c = "{1} {0} {1}".format(a, b)
#c = a + ' ' + b
#c = f"{a} {b}"
#print(c)

#a = "1"
#b = "2"
#c = int(a) + int(b)
#print(c)

# a = int(input("Primul nr: "))
# b = int(input("Al doilea nr: "))
# c = a + b
# print(c)

         # Structuri

    # if conditie:
    #     executie
    # elif conditie;
    #     executie2
    # else:
    #     executie3

# a = 2
# b = a
# a = 3
# print(a)
# print(b)
# if a is b:
#     print("a este adevarat")
# elif a > b:
#     print("a este mai mare")
# else:
#     print("a este mai mic")


    # while conditie:
    #     sintaxa1
    #     ...
    #     sintaxa2

# x = 10
# while x > 1:
#     print("x este", x)
#     #break
#     pass
#     x -= 1

# while True:
#     euro = input("Valoare euro pentru convertire: ")
#
#     if euro.isdigit():
#         pass
#     elif len(euro.split(".")) == 2:
#         a = euro.split('.')[0]
#         b = euro.split('.')[1]
#
#     if type(euro) == float:
#         euro = int(euro)
#         print("Valoare convertita este: ", euro * 4.82, "RON")
#     else:
#         print("Valoarea nu este un numar")

# str = "abecedar"
# print(str[-1])
# print(str[::-1])
# print(str[::2])
# print(str[2::])
#
# for poz, char in enumerate(str):
#     print(poz, char)

# ok = "1"
##Var 2
# while ok == "1":
#     print("1.Faceti conversie")
#     print("2.Iesiti din program")
#     ok = input()
#
#     if ok.isdigit() and int(ok) == 1:
#         euro = input("Valoare euro pentru convertire: ")
#         if len(euro) > 0:
#             floatSign = 1
#             if euro[0] == "-":
#                 floatSign = -1
#                 euro = euro[1:]
#             a = None
#             if euro.isdigit():
#                 euro = int(euro)
#             elif "." in euro and len(a := euro.split(".")) == 2 and a[0].isdigit() and a[1].isdigit():
#                 euro = float(euro)
#             else:
#                 print("Valoarea nu este un numar")
#                 continue
#             print("Valoarea convertita este:", floatSign * euro * 4.87, " RON")

for x in range(-1, 6, 2):
    print(x)

lista = list(range(10))
print(lista)