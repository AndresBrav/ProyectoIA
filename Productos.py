class Producto:
    def __init__(self, nombre, cantidad, precio_unitario):
        self.NombreProducto = nombre
        self.cantidad = cantidad
        self.PrecioUnitario = precio_unitario

    def get_nombre(self):
        return self.NombreProducto

    def get_cantidad(self):
        return self.cantidad

    def get_precio_unitario(self):
        return self.PrecioUnitario

    def Comprar(self, cantidadCoprada):
        self.cantidad = self.cantidad - cantidadCoprada
