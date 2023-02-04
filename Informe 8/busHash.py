class tabla_hash:
    def _init_(self):
        self.tabla = [None] * 200

    # Función hash
    def Hash_func(self, valor):
        llave = 0
        for i in range(0, len(valor)):
            llave += ord(valor[i])
        return llave % 200

    def Insertar(self, valor):  # Metodo para ingresar elementos
        hash = self.Hash_func(valor)
        if self.tabla[hash] is None:
            self.tabla[hash] = valor
        # else:
        #     i=0
        #     while item is not None: #Solution with Linear Probing
        #         if item[i] == valor:
        #             self.tabla[valor]
        #             item[i+1]
        #             item = self.tabla[valor]

    def Buscar(self, valor):  # Metodo para buscar elementos
        hash = self.Hash_func(valor)
        if self.tabla[hash] is None:
            return None
        else:
            return id(self.tabla[hash])

    def Quitar(self, value):  # Metodo para eleminar elementos
        hash = self.Hash_func(value)
        if self.tabla[hash] is None:
            print("No hay elementos con ese valor", value)
        else:
            print("Elemento con valor", value, "fue eliminado")
            self.tabla[hash] is None

    def _str_(self):
        return self.tabla


H = tabla_hash()
H.Insertar("Yeltsin")
H.Insertar("Luis")
H.Insertar("Kevin")
H.Insertar("Jhon")
print(H.Buscar("Yeltsin"))
print(H.Buscar("Luis"))
print(H.Buscar("Kevin"))
print(H.Buscar("Jhon"))

print(H.Buscar("Richard"))

H.Quitar("Yeltsin")
