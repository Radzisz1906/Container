import random

print("A, stala ladownosc")

conteiners = int(input("Numbers of conteiners: "))
max_conteiner_value = int(input("Max weight of conteiner: "))
ship_capacity = int(conteiners * max_conteiner_value * 0.3)

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
    plik.write("\n")
plik.close()

print("B, stala liczba kontenerow")

conteiners = int(input("Numbers of conteiners: "))
max_conteiner_value = int(input("Max weight of conteiner: "))
ship_capacity = int(conteiners * max_conteiner_value * 0.05)

plik = open("statkiB.txt", "w")
ship_line = str(ship_capacity), " ", str(conteiners)

plik.write(str(ship_capacity))
plik.write(" ")
plik.write(str(str(conteiners)))
plik.write(str("\n"))

for i in range(conteiners):
    plik.write(str(str(i + 1)))
    plik.write(" ")
    plik.write(str(random.randint(1, max_conteiner_value)))
    plik.write("\n")
plik.close()
