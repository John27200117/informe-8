#Busqueda secuencial con while
listaDeBusqueda = [5,10,1,6,9,41,21,4,8,32,24,14]
elementoBuscado = 41

indice =0
encontrado = False
posElementoBuscado = 0

#utilizamos el while...

while(indice< len(listaDeBusqueda) and encontrado ) ==False:
    print("Buscando en la posición...", indice)

    if (listaDeBusqueda[indice]==elementoBuscado):
        posElementoBuscado= indice
        encontrado = True
    indice +=1

#fin de la busqueda secuncial

if encontrado ==True:
    print("El", elementoBuscado , "fue encontrado en posición ", str(posElementoBuscado) )

else:
    print("El", elementoBuscado, "No fue encontrado")