class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        return
    
    def get_area(self):
        self.area = self.width * self.height
        return self.area
    
    def get_perimeter(self):
        self.perimeter = 2 * (self.height + self.width)
        return self.perimeter
    

altura = int(input("Ingrese la altura: "))
ancho = int(input("Ingrese el ancho: "))

rectangle = Rectangle(altura, ancho)

print(rectangle.get_area()) #75000
print(rectangle.get_perimeter()) #1100


