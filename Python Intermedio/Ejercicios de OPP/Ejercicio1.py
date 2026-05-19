# Calculating the area of a circle

class Circle:
    radius = 4

    def get_area(self):
        self.area = 3.141516 * (self.radius ** 2) 
        print(f" The radius is {self.radius}")
        return self.area

area = Circle()
print(f"The area of a circle with radius {area.radius} is {area.get_area()}") 