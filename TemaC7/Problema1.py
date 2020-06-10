
class Catalog:

    def __init__(self, prenume: str, nume: str):
        self.materii = {}
        self.absente = 0
        self.nume = nume
        self.prenume = prenume

    def incAbsente(self, nr):
        self.absente += nr

    def stergAbsente(self, nr):
        if self.absente >= nr:
            self.absente -= nr
        elif self.absente < nr:
            nr = self.absente
            self.absente -= nr

    def __str__(self):
        return f"{self.nume} {self.prenume} are: {self.absente} absente"


class Materie(Catalog):

    def __init__(self, nume: str, prenume: str):
        Catalog.__init__(self, nume, prenume)

    def adaugare(self, materie: str, nota: list):
        self.materii.update({materie: nota})

    def afisMaterii(self):
        mat = []
        for x in self.materii:
            mat.append(x)
        return f'Studentul {self.nume} {self.prenume} are materiile: ' + ', '.join(mat)

    def medieMaterie(self):
        print(f'Studentul {self.nume} {self.prenume} are la meteria: ')
        for x in self.materii:
            suma = 0
            nr = 0
            for y in self.materii[x]:
                try:
                    suma += int(y)
                    nr += 1
                except ValueError:
                    pass
            medie = suma/nr
            print(f'{x}, media: {round(medie)}')


st1 = Materie("Ion", "Roata")
st1.incAbsente(3)
st1.stergAbsente(2)
st2 = Materie("George", "Cerc")
st2.incAbsente(4)
st2.stergAbsente(2)
print(st1)
print(st2)
st1.adaugare("Python", [7, 9, 10])
st2.adaugare("Python", [8, 5, 9])
st2.adaugare("Matematica", [5, 7, 7])
st1.adaugare("Romana", [7, 9, 9])
print(st1.afisMaterii())
print(st2.afisMaterii())
st1.medieMaterie()
st2.medieMaterie()
