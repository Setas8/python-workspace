
next = True
lista = []
while next:
    nota = int(input("Mark: "))
    if nota>=0 and nota<11:
        lista.append(nota)
    if len(lista) == 5:
        next= False

print("Avg: ",sum(lista)/5, "\nMax: ", max(lista), "\nMin: ", min(lista), "\nList: ",lista)
