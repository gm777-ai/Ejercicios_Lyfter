class Walker:
    def walk(self):
        return "The character is walking."


class Swimmer:
    def swim(self):
        return "The character is swimming."


class Flyer:
    def fly(self):
        return "The character is flying."


class Attacker:
    def attack(self):
        return "The character is attacking."


class Dragon(Walker, Flyer, Attacker):
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return f"Dragon name: {self.name}"


class Mermaid(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return f"Mermaid name: {self.name}"


class SuperHero(Walker, Swimmer, Flyer, Attacker):
    def __init__(self, name):
        self.name = name

    def show_info(self):
        return f"Superhero name: {self.name}"



dragon = Dragon("FireStorm")
mermaid = Mermaid("Aqua")
hero = SuperHero("SkyBlade")

print(dragon.show_info())
print(dragon.walk())
print(dragon.fly())
print(dragon.attack())

print(mermaid.show_info())
print(mermaid.walk())
print(mermaid.swim())

print(hero.show_info())
print(hero.walk())
print(hero.swim())
print(hero.fly())
print(hero.attack())