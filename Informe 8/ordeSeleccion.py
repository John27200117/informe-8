# Ordenamiento Por Selección
lista = [5,7,3,1,8,4,9,2,6]
longitud = len(lista)

for i in range (longitud):
    print(lista)
    menor = 1
    print("El indice actual para comparar es", menor)
    for j in range (i+1, longitud):
        if lista[j] < lista[menor]:
            menor = j
            print("Recorriendo lista. Es menor el indice",menor)
    
    temporal = lista[menor]
    lista[menor] = lista[i]
    lista[i] = temporal
    print("Cambiamos el elemento", lista[menor], "por el elemento", lista[i])

print(lista)

def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


print("------ EJEMPLO DE LA DIAPOSITIVA ------\n""Lista = ",[45,52,21,37,49])
print("Lista_Ordenada = ",selection_sort([45,52,21,37,49]))

print("------ EJEMPLO DEl CÓDIGO ------\n""Lista = ",[5,7,8,4,9,2,6])
print("Lista_Ordenada = ",selection_sort([5,7,8,4,9,2,6]))