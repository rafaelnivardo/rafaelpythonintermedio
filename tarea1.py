class Producto():
    moneda = "MXN"
    def __init__(self, nombre, precio, cantidadeninventario):
        self.nombre = nombre
        self.precio = precio
        self.cantidadeninventario = cantidadeninventario

    def valor_total(self):
        return self.precio * self.cantidadeninventario

manzana = Producto("Manzana", 15, 10)
print(manzana.nombre, manzana.valor_total(), manzana.moneda)

platano = Producto("Plátano", 2, 10)
print(platano.nombre, platano.valor_total(), platano.moneda)

frutilla = Producto("Frutilla", 1, 25)
print(frutilla.nombre, frutilla.valor_total(), frutilla.moneda)
