
class Product:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        

class Inventory:
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def show_products(self):
        for product in self.product_list:
            print(f"Nombre: {product.nombre}, Precio: {product.precio}, Cantidad: {product.cantidad}")

    def calculate_total_value_of_inventory(self):
        total_value = 0

        for product in self.product_list:
            total_value += product.precio * product.cantidad

        return total_value
        


product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

product = Inventory()

product.add_product(product1)
product.add_product(product2)


product.show_products()

print(product.calculate_total_value_of_inventory())
