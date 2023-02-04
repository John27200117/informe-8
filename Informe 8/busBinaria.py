def busquedaBinaria(lista, valor):
    pasos = 0
    izq = 0
    der = len(lista)-1
    while izq <= der:
        pasos += 1
        puntoMedio = (izq + der) // 2
        if lista[puntoMedio] == valor:
            return "Valor encontrado en {} pasos, en la posicion {}.".format(pasos,puntoMedio)
        if lista[puntoMedio] > valor:
            der = puntoMedio - 1
        if lista[puntoMedio] < valor:
            izq = puntoMedio + 1
    return "Elemento no encontrado"

lista = [2,4,6,8,10,12,14,16,18]
posicion = busquedaBinaria(lista,2)
print(posicion)