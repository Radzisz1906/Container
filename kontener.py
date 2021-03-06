from collections import defaultdict
from generator import gen
import timeit
import math


class plecak():

    def __init__(self, matrix):
        self.kontenery = matrix[1:]
        self.ladownosc = matrix[0][0]
        self.ilosc = matrix[0][1]

    def zach(self):
        d = defaultdict(list)
        sor = []
        su = 0
        war = 0
        for i in self.kontenery:
            d[i[2] / i[1]] = [i[0], i[1], i[2]]
        for i in sorted(d.keys(), reverse=True):
            if su + d[i][1] <= self.ladownosc:
                sor.append(d[i][0])
                su += d[i][1]
                war += d[i][2]
            # else:
                # break
        # print(sor)
        # print(war)
        return war


def dynamic(waga, wartosc, pojemnosc, l_kontenerow):
    tabela = [[0 for x in range(pojemnosc + 1)]
              for y in range(l_kontenerow + 1)]
    for i in range(1, l_kontenerow + 1):
        for j in range(1, pojemnosc + 1):
            if j < waga[i - 1]:
                tabela[i][j] = tabela[i - 1][j]
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i - 1]
                                   [j - waga[i - 1]] + wartosc[i - 1])
    #print(tabela[l_kontenerow][pojemnosc], end=";")
    return tabela[l_kontenerow][pojemnosc]


print("1.Generuj plik i działaj. \n2.Działaj na istniejącym. \n")
wyb = int(input())
if wyb == 1:
    print("Max ladownosc statku: ")
    ladownosc = int(input())
    print("Ilosc kontenerow:")
    ilosc_kont = int(input())

sumy_d = [0] * 15
sumy_z = [0] * 15
for i in range(10):
    for z in range(1, 16):
        gen(ilosc_kont * z, ladownosc)
        dane = []
        waga = []
        wartosc = []
        plik = open("statkiA.txt")
        i = 0
        for line in plik:
            tmp = line.split()
            tmp = list(map(int, tmp))
            dane.append(tmp)
            if i > 0:
                waga.append(tmp[1])
                wartosc.append(tmp[2])
            i += 1
        plik.close()
        p = plecak(dane)
        print(timeit.timeit(lambda: dynamic(
            waga, wartosc, p.ladownosc, p.ilosc), number=1), end=";")
        print(timeit.timeit(lambda: p.zach(), number=1))
        # print(math.floor())
        dyn = dynamic(waga, wartosc, p.ladownosc, p.ilosc)
        zach = p.zach()
        sumy_d[z - 1] += dyn
        sumy_z[z - 1] += zach
for i in range(15):
    print(sumy_d[i] / 10, ";", sumy_z[i] / 10)
