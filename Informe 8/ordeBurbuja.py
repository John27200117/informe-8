#ORDENAMIENTO POR BURBUJA
lista = [5,7,3,1,8,4,9,2,6]
print("Lista = ",lista)
for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        print("Comparando:",lista[j],"con",lista[j+1])
        
        if lista[j] > lista[j+1]:
            temporal = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temporal
            
            print("Intercambiando",lista[j],"por",lista[j+1])
            
print("Lista Ordenada = ",lista)