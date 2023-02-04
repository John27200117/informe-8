from random import randint, random

lista=[]
for i in range (1,10):
    lista.append(randint(1,40))


print(lista)

def buscador(c,d):
    cont=0
    for i in c:
        if i==d:
            print("ya lo encontré...")
            print("se encuentra en la posicion:",cont)
            break
        else:
            cont +=1
            continue
    if cont==len(lista):
        print("El digito ",d," no existe en la lista:",lista)

dato=int(input("qué numero de la lista quire buscar? :"))
buscador(lista,dato)
