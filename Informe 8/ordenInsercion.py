"""Algoritmos de ordenamiento por inserción """
_listaD = [45, 52, 21, 37, 49]
_tamanioL = (len(_listaD))

print(_listaD)

for i in range(1, _tamanioL):
    aux = _listaD[i]
    j=i
    while j>0 and aux<_listaD[j-1]:
        _listaD[j] = _listaD[j-1]
        j-=1
        _listaD[j]=aux
        print(_listaD)
    print(_listaD)
    
