import random


def gen(conteiners, max_conteiner_value):
    print("A, stala ladownosc")
    ship_capacity = max_conteiner_value

    plik = open("statkiA.txt", "w")
    ship_line = str(ship_capacity), " ", str(conteiners)

    plik.write(str(ship_capacity))
    plik.write(" ")
    plik.write(str(str(conteiners)))
    plik.write(str("\n"))

    for i in range(conteiners):
        plik.write(str(str(i + 1)))
        plik.write(" ")
        plik.write(str(random.randint(1, max_conteiner_value)))
        plik.write(" ")
        plik.write(str(random.randint(1, 100)))
        plik.write("\n")
    plik.close()
