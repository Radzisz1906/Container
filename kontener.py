from collections import defaultdict


class plecak():

    def __init__(self, lad, kont):
        self.kontenery = []
        self.ladownosc = lad
        self.ilosc = kont

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
    if i == 0:
        p = plecak(int(line.split()[0]), int(line.split()[1]))
        i += 1
    else:
        tmp = line.split()
        tmp = list(map(int, tmp))
        p.kontenery.append(tmp)
plik.close()
p.zach()
