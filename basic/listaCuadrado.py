from random import randint
from math import pow

lista1 = []
lista2 = []
lista3 = []
for num in range(1,11):
    aleatorio = randint(1,100)
    lista1.append(aleatorio)
    lista2.append(pow(aleatorio,2))
    lista3.append(pow(aleatorio,3))
for num in range(0,10):
    print(lista1[num], lista2[num], lista3[num])