from collections import defaultdict


class plecak():

    def __init__(self, matrix):
        self.kontenery = matrix[1:]
        self.ladownosc = matrix[0][0]
        self.ilosc = matrix[0][1]

    def zach(self):
        d = defaultdict(list)
        sor = []
        su = 0
        for i in self.kontenery:
            d[i[2] / i[1]] = [i[0], i[1], i[2]]
        for i in sorted(d.keys(), reverse=True):
            if su + d[i][1] <= self.ladownosc:
                sor.append(d[i][0])
                su += d[i][1]
            else:
                break
        print(sor)


dane = []
plik = open("statkiA.txt")
i = 0
for line in plik:
    tmp = line.split()
    tmp = list(map(int, tmp))
    dane.append(tmp)
p = plecak(dane)
plik.close()
p.zach()
