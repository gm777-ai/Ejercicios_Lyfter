class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def agregar_pasajero(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} got on the bus.")
            print(f"Current passengers: {len(self.passengers)}")
        else:
            print("The bus is full.")

    def bajar_pasajero(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} got off the bus.")
            print(f"Current passengers: {len(self.passengers)}")
        else:
            print(f"{person.name} is not on the bus.")


bus = Bus(3)

person_1 = Person("Carlos")
person_2 = Person("Ana")
person_3 = Person("Luis")
person_4 = Person("Maria")

bus.agregar_pasajero(person_1)
bus.agregar_pasajero(person_2)
bus.agregar_pasajero(person_3)
bus.agregar_pasajero(person_4)

bus.bajar_pasajero(person_2)
bus.agregar_pasajero(person_4)