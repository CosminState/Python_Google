    # Functii

# def prima_functie():
#     #corpul functiei
#     pass


# def message():
#     print("Enter a value: ")

#message = 1


# def hello(name = 'Cosmin'):   # parametrul e "name"
#     print("hello", name)
#
# name1 = input("Enter your name: ")
#
# hello(name1)        # argumentul e "name1"


# def message(what='phone', number='2'):
#     """
#     :param what:
#     :param number:
#     :return:
#     """
#     print("Enter", what, "number", number)
#
#
# message(number = '3', what = 'number')

# def suma(a, b, c):
#     print(f"{a} + {b} + {c} =", a + b + c)
#
# suma(3, c = 1, b = 2)

# def HappyNewYear(wishes = True):
#     print('3')
#     print('2')
#     print('1')
#     if not wishes:
#         return
#     print("Happy new year!")
#
# HappyNewYear()

# def name():
#     return 123
#
#
# a = name()
# print(a)

# def sumOfList(lst):
#     sum = 0
#     for elem in lst:
#         sum += elem
#     return sum
#
#
# a = sumOfList([5, 4, 3])
# print(a)

# def litere(litera: str) -> bool:    # recomandata ca param de intrare sa fie string, iar cel de iesire boolean
#     if isinstance(litera, str):
#         return True
#     else:
#         return '23'
#
# a = litere('3')
# print(a)

# import calendar
#
# def an_bisect(an: int) -> bool:
#     if calendar.isleap(an):
#         return True
#     return False
#
# an = input('Introduceti anul: ')
#
# try:
#     an = int(an)
# except ValueError:
#     print("Nu ati introdus un numar")
#
# print("Anul este biset" if an_bisect(an) else "Anul nu este bisect")

# import datetime
# import sys
#
# def validareNrZile(zi, luna, an) -> bool:
#     try:
#         a = datetime.datetime.strptime(f'{zi}.{luna}.{an}', "%d.%m.%Y")
#         print(a)
#         exit
#     except Exception as e:
#         # return False
#         print("except", e)
#         pass
#     else:
#         print("else")
#     finally:
#         return False
#
# a= validareNrZile(23, 7, 2020)
# print(a)

# def isPrime(number: int) -> bool:
#     # exista si functia isPrime
#
#     if number < 2:
#         return False
#     elif number == 2:
#         return True
#     else:
#         i = 2
#         while i * i <= number:
#             if number % i == 0:
#                 return False
#             i += 1
#         return True
#
# print(isPrime(3))

# def muliply(a, b):
#     return
#
# print(muliply(3, 4))

# def wishes():
#     print('My wishes')
#     return 'Happy'
#
# print(wishes())
# w = wishes()
# print(w)

# def Hi(MyLIST):
#     for name in MyLIST:
#         print(f'Hi, {name}')
#         return 'a'
#
# a = Hi(['Adam', 'Spongebob', 'Mr. Krabs'])
# print(a)

# def createList(n):
#     myList = []
#     for i in range(n):
#         myList.append(i)
#     return myList
#
#
# print(createList(5))

# def hi():
#     return
#     #print('Hi')
#
# hi()

# def isInt(DATA):
#     if type(DATA) == int:
#         return True
#     elif type(DATA) == float:
#         return False
#
# print(isInt(5))
# print(isInt(5.0))
# print(isInt('5'))

# def evenNumLst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
#
# print(evenNumLst(11))

# def listUpdater(lst):
#     updList = []
#     for elem in lst:
#         elem **= 2
#         updList.append(elem)
#     return updList
#
# l = [1, 2, 3, 4, 5]
# print(listUpdater(l))

# def scopeTest():
#     x = 123
#
# scopeTest()
# print(x)
################
# var = 3         # namespace la nivel global
# def myFunction():
#     # global var
#     var = 2         # namespace la nivel de functie
#     print('Var este: ', var)
#     return var
#
#
# # var = 1
# myFunction()
# print(var)
################

# var = 2
# print(var)
# def multByVar():
#     global var
#     var = 5
#     return var
#
# var = 3
# # print(multByVar(7))
# print(multByVar())
# print(var)
################

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# print(factorial(4))
# 4 * factorial(3)
# 4 * 3 * factorial (2)
# ...
# 4 * 3 * 2 * 1 = 24
################

# def fun(a):
#     if a > 30:
#         return 3
#     else:
#         return a + fun(a + 3)
#
# print(fun(25))
# # 25 + 28 + 3 = 56
################

# def sum(a, b):
#     return a + b, a * b
#
# x, y = sum(2, 3)
# print(x, y)