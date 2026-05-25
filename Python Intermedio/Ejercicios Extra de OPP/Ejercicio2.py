class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    
    def get_area(self):
        self.area = self.width * self.height
        return self.area 
    
    def get_perimeter(self):
        self.perimeter = 2 * (self.height + self.width)
        return self.perimeter
    



try:

    altura = int(input("Ingrese la altura: "))
    ancho = int(input("Ingrese el ancho: "))
    if altura < 0 or ancho < 0:
        raise TypeError()
    
    elif altura >= 0 and ancho >= 0:
        rectangle = Rectangle(altura, ancho)
        print(f"El area es: {rectangle.get_area()}") #75000
        print(f"El perimetro es: {rectangle.get_perimeter()}") #1100

except TypeError:

    print("Existe un valor negativo, los valores deben ser positivos")





