from operator import itemgetter


class CatalocPrajituri:
    prajituri = []

    def __init__(self, nume: str, gramaj: int, pret: int):
        self.nume = nume
        self.gramaj = gramaj
        self.pret = pret
        self.prajituri.append([nume, gramaj, pret])

    def gramajPraji(self):
        print("Sortare dupa gramaj:")
        return sorted(self.prajituri, key=itemgetter(1))

    def pretPraji(self):
        print("Sortare dupa pret:")
        return sorted(self.prajituri, key=itemgetter(2))


class Tort(CatalocPrajituri):

    def __init__(self, nume: str, gramaj: int, pret: int, etajat = False, glazura = 'ciocolata'):
        CatalocPrajituri.__init__(self, nume, gramaj, pret)
        self.etajat = etajat
        self.glazura = glazura

    def setAtribut(self, etajat: bool, glazura: str):
        self.etajat = etajat
        self.glazura = glazura

    def getAtribut(self):
        return f'Tortul: {self.nume} este etajat: {self.etajat} si are glazura: {self.glazura}'


class Fursec(CatalocPrajituri):

    def __init__(self, nume: str, gramaj: int, pret: int):
        CatalocPrajituri.__init__(self, nume, gramaj, pret)


ob1 = Tort('Tort de ciocolata', 40, 10)
ob2 = Tort('Tort diplomat', 20, 6)
ob3 = Tort('Tort de vanilie', 35, 15)
ob4 = Fursec('Fursec maro', 2, 2)
ob5 = Fursec('Fursec negru', 2, 4)
ob6 = Fursec('Fursec alb', 2, 3)
print(ob6.gramajPraji())
print(ob6.pretPraji())
ob2.setAtribut(True, 'cacao')
print(ob2.getAtribut())
ob1.setAtribut(True, 'capsuna')
print(ob1.getAtribut())



